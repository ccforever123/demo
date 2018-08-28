from selenium import webdriver

url = 'http://m.dianping.com/shop/23484402'
driver = webdriver.Firefox()
driver.get(url)
print(driver.page_source)
driver.quit()
