from selenium import webdriver
import time

def main():
    login_url = 'https://hwid1.vmall.com/CAS/portal/login.html'
    current_url = login(login_url)
    print(current_url)


def login(url):
    phone = ''
    pw = ''
    driver = webdriver.Chrome()
    driver.get(url)
    driver.find_element_by_name('userAccount').send_keys(phone)
    driver.find_element_by_name('password').send_keys(pw)
    driver.find_element_by_class_name('button-login').click()
    while driver.current_url == url:
        time.sleep(3)
        continue
    cookies = driver.get_cookies()
    print(cookies)
    return driver.current_url

def login1(url):
    pass

if __name__ == '__main__':
    main()