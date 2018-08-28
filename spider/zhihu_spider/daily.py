from urllib.parse import urljoin
import requests
from selenium import webdriver
import re
import os



def get_html(url):
	driver = webdriver.PhantomJS()
	driver.get(url)
	html = driver.page_source
	driver.quit()
	return html

def get_index(url):
	index_html = get_html(url)
	reg_title = re.compile(r'<span class=\"title\">(.*?)</span>')
	reg_link = re.compile(r'<div class=\"box\"><a href=\"(.*?)\" class=\"link-button\">')
	title_list = reg_title.findall(index_html)
	link_list = reg_link.findall(index_html)
	for i in range(len(link_list)):
		link_list[i] = urljoin(url, link_list[i])
	index_list = zip(title_list, link_list)
	for page_tuple in index_list:
		get_page_detail(page_tuple)

def get_page_detail(page_tuple):
	title = page_tuple[0]
	url = page_tuple[1]
	page_html = get_html(url)
	reg_author = re.compile(r'<span class=\"author\">(.*?)，</span>')
	reg_bio = re.compile(r'<span class=\"bio\">(.*?)</span>')
	reg_content = re.compile(r'<span class="bio">.*?<div class=\"content\">(.*?)</div>', re.S)
	author = reg_author.findall(page_html)[0]
	bio = reg_bio.findall(page_html)[0]
	# content需要皮牌多行，使用re.S
	content = reg_content.findall(page_html)[0]
	print(title)
	print('********** %s , %s **********' % (author, bio))
	save_to_file(title, author, bio, content)
	print('----------------------------END----------------------------')

def save_to_file(title, author, bio, content):
	with open('%s.html' % title, 'w') as f:
		f.write('Title: %s \n' % title)
		f.write('Author: %s , %s \n' % (author, bio))
		f.write(content)
		
	


def main():
	url = 'http://daily.zhihu.com/'
	get_index(url)


if __name__ == '__main__':
	main()