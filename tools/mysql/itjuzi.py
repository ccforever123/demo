import pymysql
from selenium import webdriver
import re

def get_company_info(driver):
	for page in range(1,20):
		print('Page %s' % page)
		driver.get('https://www.itjuzi.com/company?page=%s' % page)
		page_source = driver.page_source
		#print(page_source)
		reg_company_info = re.compile(r'<li data-id=\"(.*?)\">.*?<div class=\"title\">.*?<span>(.*?)</span>.*?<span class=\"rounder\">(.*?)</span>.*?<div class=\"line2\">(.*?)</div>.*?<p class=\"des\"><span>(.*?)</span></p>.*?<i class=\"cell date\">\n\t\t\t\t\t\t\t\t(.*?)\t\t\t\t\t\t\t</i>.*?<i class=\"cell place\">\n\t\t\t\t\t\t\t\t(.*?)\t\t\t\t\t\t\t</i>.*?<i class=\"cell classify\">\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t(.*?)\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t</i>',re.S)
		company_list = reg_company_info.findall(page_source)
		#print(company_list)
		inist = save_to_sql(company_list)
		if inist == 1:
			break

def save_to_sql(company_list):
	for i in company_list:
		company_id = i[0]
		company_name = i[1]
		founder = i[2][2:-2]
		more_info = i[3][:-1]
		info = i[4]
		found_date = i[5]
		place = i[6]
		category = i[7]
		#print(i)
		db = pymysql.Connect('localhost','root','123456','test', charset="utf8")
		cursor = db.cursor()
		'''
		cursor.execute("DROP TABLE IF EXISTS company_list")

		create_sql = """CREATE TABLE company_list (
			         company_id  INT NOT NULL,
			         company_name  VARCHAR(255),
			         found_date  VARCHAR(255),
			         place  VARCHAR(255),
			         category  VARCHAR(255),
			         founder  VARCHAR(255),
			         info  VARCHAR(255),
			         more_info  VARCHAR(255))"""

		cursor.execute(create_sql)
		'''
		find_sql = "SELECT * FROM company_list WHERE company_id=%s"
		if cursor.execute(find_sql, company_id) == 0:
			insert_sql = "INSERT INTO company_list VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
			try:
				cursor.execute(insert_sql, (company_id, company_name, found_date, place, category, founder, info, more_info))
				db.commit()
				print('===%s 添加成功===' % company_name)
			except:
				db.rollback()
				print('===！！！%s 添加失败！！！===' % company_name)
		else:
			print('%s 已存在' % company_name)
			#cursor.close()
			#db.close()
			#return 1
		cursor.close()
		db.close()
	return 0

def main():
	driver = webdriver.PhantomJS()
	get_company_info(driver)
	driver.quit()


if __name__ == '__main__':
    main()