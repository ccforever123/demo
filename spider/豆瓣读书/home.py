import requests
import re
import json
from openpyxl import Workbook


def get_html_data(url):#解析网页
	r = requests.get(url)
	r.encoding = r.apparent_encoding
	return r.text

def get_tags(index_data):#获取tag
	with open('tag.json', 'w', encoding='utf-8') as f:
		reg_tags = r'<a href=\"/tag/(.*?)\">(.*?)</a>'
		tag_list = re.findall(reg_tags, index_data)
		tag_dict = {}
		for i,j in tag_list:
			i = 'https://book.douban.com/tag/' + i
			tag_dict[j] = i
		json.dump(tag_dict, f)
		print('Tag data saved.')

def get_book_list_page():#获取标签下的图书链接列表
	with open('tag.json', 'r', encoding='utf-8') as f:
		tags_dict = json.load(f)
		for tag_info in tags_dict:
			tag, tag_link = tag_info, tags_dict[tag_info]
			book_list_data = get_html_data(tag_link)




def main():
	url = 'https://book.douban.com/tag/'
	index_data = get_html_data(url)
	get_tags(index_data)
	get_book_list_page()


if __name__ == '__main__':
	main()