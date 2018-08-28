import pymysql
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.proxy import Proxy
from selenium.webdriver.common.proxy import ProxyType
import re
import random
import time

def Chrome_proxy():
	PROXY = "60.255.186.169:8888"  # IP:PORT or HOST:PORT
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument('--proxy-server=http://%s' % PROXY)
	return chrome_options

def get_company_info(driver, start_id):
	for company_id in range(start_id,1000):
		try:
			url = 'https://www.itjuzi.com/company/%s' % company_id
			print('正在打开网页：%s' % url)
			driver.get(url)
			page_source = driver.page_source
			#reg_header = re.compile(r'<title>(.*?)</title>')
			#header = reg_header.findall(page_source)[0]

			#print(page_source)
			reg_company_name = re.compile(r'<h1 class=\"seo-important-title\">\n\t\t\t\t\t\t\t\t\t(.*?)\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<span class=\"t-small c-green\">\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t(.*?)\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t</span>',re.S)
			company_info = reg_company_name.findall(page_source)[0]
			company_name = company_info[0]
			founder = company_info[1]
			print('公司名：%s' % str(company_info))

			reg_category = re.compile(r'c-gray\"></i>.*?<a href=.*?_blank\">(.*?)</a>', re.S)
			category = reg_category.findall(page_source)[0]
			print('分类：%s' % category)

			reg_slogan = re.compile(r'<h2 class=\"seo-slogan\">(.*?)</h2>', re.S)
			slogan = reg_slogan.findall(page_source)[0]
			print('口号：%s' % slogan)

			reg_locate = re.compile(r'<span class=\"loca c-gray-aset\">.*?>(.*?)</a>', re.S)
			locate = reg_locate.findall(page_source)[0]
			print('所在地：%s' % locate)

			reg_tag = re.compile(r'<a href="https://www.itjuzi.com/tag/.*?"><span class="tag">(.*?)</span></a>')
			tags = str(reg_tag.findall(page_source))
			print('标签：%s' % tags)

			reg_info = re.compile(u'<!-- 公司简介 -->.*?<div class=\"block\">(.*?)</div>.*?<!-- 公司简介结束 -->', re.S)
			info = reg_info.findall(page_source)
			print('介绍：%s' % info)

			reg_second_title = re.compile(r'公司全称：(.*?)</h2>.*?成立时间：(.*?)</h2>.*?公司规模：(.*?)\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t</h2>', re.S)
			second_title = reg_second_title.findall(page_source)[0]
			full_name = second_title[0]
			found_date = second_title[1]
			employee = second_title[2]
			print('全名：%s' % str(second_title))

			reg_status = re.compile(r'(closed)')
			status = reg_status.findall(page_source)
			print('状态：%s' % status)

			company_detail = (company_id, company_name, founder, category, slogan, locate, tags, info, full_name, found_date, employee, status)
			#print(company_detail)

			print('正在将 %s 的数据保存到数据库' % company_name)
			save_to_sql(company_detail)
			#delay = random.randint(5,20)
			#for t in range(delay):
			#	print('等待 %s 秒' % (delay-t))
			#	time.sleep(1)
		except:
			if driver.title == 'WAF验证页面':
				check_ip(company_id)
			continue

def check_ip(count_ip):
	driver = webdriver.PhantomJS()
	driver.get('http://www.xicidaili.com/nn/')
	source = driver.page_source
	reg_ip = re.compile('<td class=\"country\"><img.*?<td>(.*?)</td>.*?<td>(.*?)</td>', re.S)
	proxy_ip_list = reg_ip.findall(source)
	#print(proxy_ip_list)


def save_to_sql(company_detail):

	company_id = company_detail[0]
	db = pymysql.Connect('localhost','root','123456','test', charset="utf8")
	cursor = db.cursor()

	cursor.execute("DROP TABLE IF EXISTS company")

	create_sql = """CREATE TABLE company (
	         company_id  INT NOT NULL,
	         company_name  VARCHAR(255),
	         founder  VARCHAR(255),
	         category  VARCHAR(255),
	         slogan  VARCHAR(255),
	         locate  VARCHAR(255),
	         tags  VARCHAR(255),
	         info  VARCHAR(255),
	         full_name  VARCHAR(255),
	         found_date  VARCHAR(255),
	         employee  VARCHAR(255),
	         status VARCHAR(255))"""

	cursor.execute(create_sql)

	find_sql = "SELECT * FROM company WHERE company_id=%s"
	if cursor.execute(find_sql, company_id) == 0:
		insert_sql = "INSERT INTO company VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
		try:
			cursor.execute(insert_sql, company_detail)
			db.commit()
			print('===%s 添加成功===' % company_detail[1])
		except:
			db.rollback()
			print('===！！！%s 添加失败！！！===' % company_detail[1])
	else:
		print('%s 已存在' % company_detail[1])
	cursor.close()
	db.close()

def main():
	#driver = webdriver.Firefox(proxy=proxy)

	chrome_options = Chrome_proxy()
	driver = webdriver.Chrome(chrome_options=chrome_options)
	#driver = webdriver.Firefox()
	get_company_info(driver, start_id='1')

	driver.quit()


if __name__ == '__main__':
    main()