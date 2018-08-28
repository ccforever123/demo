import requests
import re


def get_text(url):
	r = requests.get(url)
	r.encoding = r.apparent_encoding
	return r.text


def get_location(name):
	url = "http://restapi.amap.com/v3/geocode/geo?key=910cc97a063204c50d509ecb492afbe1&address=%s&city=厦门" % name
	text = get_text(url)
	reg_locate = re.compile(r'location\":\"(.*?)\"')
	locate_list = reg_locate.findall(text)
	if len(locate_list) == 0:
		print('没有找到该地址')
	elif len(locate_list) == 1:
		locate = locate_list[0]
		return locate
	else:
		print('请重新输入如下地址：')
		print(locate_list)
		main()

def get_shop_info(locate):
	url = 'http://restapi.amap.com/v3/place/around?key=910cc97a063204c50d509ecb492afbe1&location=%s&output=xml&radius=300&types=冷饮店&extensions=base' % locate
	text = get_text(url)
	reg_name = re.compile(r'<name>(.*?)</name>.*?<distance>(.*?)</distance>')
	name_list = reg_name.findall(text)
	for i in range(len(name_list)):
		print("%s %s : %s" % (i+1, name_list[i][0], name_list[i][1]))
#		with open('name.txt', 'a', encoding='utf-8') as f:
#			f.write("%s %s : %s \n" % (i+1, name_list[i][0], name_list[i][1]))

def main():
	name = input('请输入地址：')
	locate = get_location(name)
	get_shop_info(locate)

if __name__ == '__main__':
    main()