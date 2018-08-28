#coding:utf-8
import urllib.request
from selenium import webdriver
from PIL import Image
import re
import time



url = 'http://accounts.douban.com/login'
email = input('E-mail:')
password = input('Password:')

browser = webdriver.PhantomJS()
browser.get(url)

#get page source
#page_source = browser.page_source

#send account key
print('writing username and password...')
browser.find_element_by_name('form_email').send_keys(email)
browser.find_element_by_name('form_password').send_keys(password)

#get captcha link and save to local
print('saving captcha image...')
captcha_link = browser.find_element_by_id('captcha_image').get_attribute('src')
urllib.request.urlretrieve(captcha_link,'captcha.jpg')
Image.open('captcha.jpg').show()
captcha_code = input('Pls input captcha code:')
browser.find_element_by_id('captcha_field').send_keys(captcha_code)

print('login...')
browser.find_element_by_name('login').click()
time.sleep(3)

if browser.current_url == 'https://www.douban.com/':
	print('login success!')
	print('Now jump to %s ...' % browser.current_url)
else:
	print('login error!')
	quit()

# visit book tag url and get page source
book_tag_url = 'https://book.douban.com/tag/'
browser.get(book_tag_url)
page_source = browser.page_source

reg_tag = r'href=\"/tag/(.*?)\"'
tag_list = re.findall(reg_tag, page_source)
print(tag_list)

browser.quit()
