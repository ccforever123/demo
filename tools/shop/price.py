# try to find the shop rent thermal diagram from 58.com

import re
from selenium import webdriver
import requests

def get_source(url):
	print('Open PhantomJS')
	driver = webdriver.PhantomJS()
	print('Open Website: %s' % url)
	driver.get(url)
	print('Get page source...')
	source = driver.page_source
	driver.quit()
	return source

def get_source_2(url):
	try:
		r = requests.get(url)
		r.encoding = r.apparent_encoding
		return r.text
	except Exception as e:
		print('Error:', e)

def get_info(source):
	reg_info = re.compile(r'<h2 class="title".*?<a href=\"(.*?)\".*?<span class=\"title_des\">(.*?)</span>.*?<span>([0-9]*?m²)</span>.*?<span>(.*?) - (.*?)</span>.*?<span>(.*?)</span>.*?<div class="time">(.*?)</div>.*?<b>(.*?)</b>', re.S)
	info_list = reg_info.findall(source)
	for (link, title, area, district, locate, addr, update, price) in info_list:
		print(link, title, area, district, locate, addr, update, price)

	reg_next = re.compile(r'<a class=\"next\" href=\"(.*?)\">')
	next_list = reg_next.findall(source)
	if len(next_list) == 1:
		next_page = next_list[0]
		return next_page
	else:
		print('Finished.')
		return 0

def main():
	next_page = 'http://xm.58.com/shangpucz/'
	source = get_source_2(next_page)
#	print(source)
	next_page = get_info(source)

#	with open('1.txt', 'r', encoding='utf-8') as f:
#		source = f.read()
#		while 'http://xm.58.com/' in next_page:
#		source = get_source(next_page)
#		next_page = get_info(source)

if __name__ == '__main__':
    main()