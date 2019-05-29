from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--headless')
import re
import requests
import time



def main():
    keyword = input('请输入关键词：')
    searchDict = {
        "jd": 'https://so.m.jd.com/ware/search.action?keyword={}'.format(keyword),
        "suning": 'https://m.suning.com/search/{}/'.format(keyword),
    }
    startSearch(keyword, searchDict)


def startSearch(keyword, searchDict):
    timestamp = int(time.time())
    now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    resultDict = {
            "timestamp": timestamp,
            "time": now,
            "productList": [],
        }

    print('timestamp: {}, {}'.format(timestamp, type(timestamp)))
    for urlTitle in searchDict:
        url = searchDict[urlTitle]
        # pageSource = getSourceByRequests(url)
        if urlTitle == 'jd':
            print('Searching @ jd.com')
            pageSource = getSourceByRequests(url)
            resultDict = getJDProductData(pageSource, resultDict)
            print('JD Data Saved')
        elif urlTitle == 'suning':
            print('Searching @ suning.com')
            pageSource = getSourceBySelenium(url)
            resultDict = getSuningProductData(pageSource, resultDict)
            print('Suning Data Saved')
    saveData(resultDict, timestamp, keyword)


def getSourceByRequests(url):
    r = requests.get(url)
    source = r.text
    # with open('source.txt', 'w', encoding='utf-8') as f:
    #     f.write(source)
    return source


def getSourceBySelenium(url):
    # driver = webdriver.PhantomJS()
    driver = webdriver.Chrome(chrome_options = chrome_options)
    driver.get(url)
    pageSource = driver.page_source
    driver.quit()
    with open('source.txt', 'w', encoding='utf-8') as f:
        f.write(pageSource)
    print('SourceCode Saved.')
    return pageSource


def getJDProductData(pageSource, resultDict):
    reg_product = re.compile(r'<div class=\"search_prolist_title\".*?>(.*?)</div>.*?pri=\"(.*?)\"></em>.*?<span id="com_.*?rd=\"0-4-1\">(.*?)</span>条评价</span>.*?class=\"shop_name\">(.*?)</span></div>', re.S)
    products = reg_product.findall(pageSource)
    # print(productList)
    for product, price, sales, shopName in products:
        productDict = {
            "productName": product.split('  ')[-1],
            "price": price,
            "sales": sales,
            "shopName": shopName
        }
        resultDict['productList'].append(productDict)
        print('{}\t{}\t{}\t{}'.format(productDict['productName'], productDict['price'], productDict['sales'], productDict['shopName']))
    return resultDict


def getSuningProductData(pageSource, resultDict):
    reg_product = re.compile(r'class=\"project-label\">(.*?)</i>(.*?)</p>.*?￥<strong>(.*?)</strong>.*?<p class=\"shop-num\">.*?<em>(.*?)条评价</em>', re.S)
    products = reg_product.findall(pageSource)
    for shopName, productName, price, sales in products:
        productDict = {
            "productName": productName,
            "price": price,
            "sales": sales,
            "shopName": '苏宁' + shopName
        }
        resultDict['productList'].append(productDict)
        print('{}\t{}\t{}\t{}'.format(productDict['productName'], productDict['price'], productDict['sales'], productDict['shopName']))
    return resultDict


def saveData(resultDict, timestamp, keyword):
    now = resultDict['time']
    for product in resultDict['productList']:
        productName = product['productName']
        price = product['price']
        sales = product['sales']
        shopName = product['shopName']
        text = '{},{},{},{},{},{}\n'.format(timestamp, now, productName, price, sales, shopName)
        with open('{}-{}.csv'.format(keyword, timestamp), 'a', encoding='gbk') as f:
            f.write(text)


if __name__ == "__main__":
    main()