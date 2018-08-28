from bs4 import BeautifulSoup
import requests
	
cookie = input('Cookie:')
header = {
	'Host': 'www.zhihu.com',
	'User-Agent': 'Mozilla/5.0(Windows NT 10.0; ...) Gecko/20100101 Firefox/53.0',
	'Accept': '*/*',
	'Accept-Language': 'zh-CH,zh;q=0.8,en-US;q=0.5,en;q=0.3',
	'Accept-Encoding': 'gzip, deflate, br',
	'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
	'X-Requested-With': 'XMLHttpRequest',
	'Referer': 'https://www.zhihu.com/',
	'Cookie': cookie
	}

data = {
	'email': '00000000',
    'password': '0000000',
	'captcha_type':	"cn",
	'_xsrf': "448a60cf850dc58a353852c70a4d53bf"
}

def login(url, data, header):
	r_get = requests.get(url)
	html = r.text
	soup = BeautifulSoup(html)
	_xsrf = soup.input
	
	r_pos = requests.post(url,data=data, headers=header)
	print(r.text)


def main():
	url = 'https://www.zhihu.com/'
	login(url, data, header)




if __name__ == '__main__':
	main()
