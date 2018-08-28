#coding:utf-8
from selenium import webdriver
import re
import random
import pymysql

def get_source(url, driver):
	driver.get(url)
	print('get page source : %s' % url)
	return driver.page_source

def get_shop_list(source):
	print('get shop list...')
	reg_shop = re.compile(r'data-hippo-type=\"shop\" title=\"(.*?)\" target=\"_blank\" href=\"(.*?)\"')
	shop_list = reg_shop.findall(source)
	return shop_list

def save_shop_data(shop_info):
	shop_name = shop_info[0]
	shop_link = 'http://m' + shop_info[1][10:]
	shop_id = int(re.sub("\D", "", shop_link))
	print(shop_id)
	db = pymysql.Connect('0', 'root', '0', 'test', charset="utf8")
	cursor = db.cursor()
	find_sql = "SELECT * FROM shop WHERE shop_id=%s"
	if cursor.execute(find_sql, shop_id) == 0:

		insert_sql = "INSERT INTO shop(shop_id, shop_name, shop_link) VALUES (%s, %s, %s)"
		try:
			cursor.execute(insert_sql, (shop_id, shop_name, shop_link))
			db.commit()
			print('%s Saved' % shop_name)
		except Exception as e:
			db.rollback()
			print('== Save %s error,\nException:%s ==' % (shop_name,e))
	else:
		print('Data exist')

		cursor.close()

def get_shop_info(source):
	shop_id = re.compile(r'shopId:(.*?)').findall(source)[0]
	shop_name = re.compile(r'<h1 class=\"shop-name\">(.*?)</h1>').findall(source)[0]
	price = re.compile(r'¥<span class=\"price\">(.*?)</span>').findall(source)[0]
	score_list = re.compile(r'<div class=\"desc\">.*?口味:(.*?)</span>.*?环境:(.*?)</span>.*?服务:(.*?)</span>', re.S).findall(source)
	addr = re.compile(r'<i class=\"icon-address\"></i>(.*?)\n').findall(source)[0]
	tel = re.compile(r'href=\"tel:(.*?)\"').findall(source)[0]
	dish_name = re.compile(r'<span class=\"goodUp\"></span>(.*?)人推荐.*?dishName\">(.*?)</div>', re.S).findall(source)[:5]
	print(shop_id, shop_name, price, score_list, addr, tel, dish_name)




def main():
	driver = webdriver.Firefox()
#	url = 'https://m.dianping.com/shoplist/15/r/0/c/117/s/s_2?from=m_nav_1_meishi'
	page = 1
	for page in range(1,50):
		print('loading page: ', page)
		url2 = 'http://www.dianping.com/search/category/15/10/g117o2p%s' % page
		source = get_source(url2, driver)
		shop_list = get_shop_list(source)
		for shop_link in shop_list:
			source = get_source(shop_link[0], driver)
			get_shop_info(shop_link[1], driver)

			sleep = random.randint(1,5)
			for sle in range(sleep):
				print(sleep-sle)

	driver.quit()

def main1():
	with open('shop_list.txt', 'r', encoding='utf-8') as f:
		source = f.read()
		shop_list = get_shop_list(source)
		save_shop_data(shop_list)

if __name__ == '__main__':
    main()