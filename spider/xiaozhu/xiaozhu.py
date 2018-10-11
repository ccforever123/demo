import requests
import re
from pymongo import MongoClient

def get_html(url):
	r = requests.get(url)
	r.encoding = r.apparent_encoding
	return r.text

def get_data(html):
	reg_info = re.compile(r'<img class=\"lodgeunitpic\" title=\"(.*?)\".*?<span class=\"result_price\">&#165;<i>(.*?)</i>', re.S)
	info_list = re.findall(reg_info, html)
	return info_list

def insert_db():
	client = MongoClient('locallost', 27017)
	db_xiaozhu = client['xiaozhu']

def main():
	house_list =[]
	for page in range(1,4):
		url='http://xm.xiaozhu.com/search-duanzufang-p%s-0/' % page
		html = get_html(url)
		info_list = get_data(html)
		for info in info_list:
			data = {}
			data['title'] = info[0]
			data['price'] = info[1]
			house_list.append(data)
	print(house_list)


if __name__ == '__main__':
    main()