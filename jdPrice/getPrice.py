from selenium import webdriver
import re
import requests
import time



def main():
    keyword = input('请输入关键词：')
    searchDict = {
        "jd": 'https://so.m.jd.com/ware/search.action?keyword={}'.format(keyword),
    }
    startSearch(keyword, searchDict)


def startSearch(keyword, searchDict):
    for urlTitle in searchDict:
        url = searchDict[urlTitle]
        # pageSource = getSourceByRequests(url)
        pageSource = getSourceBySelenium(url)
        resultDict = getJDProductData(pageSource)
        for item in resultDict['productList']:
            print('{}\t{}\t{}\t{}'.format(item['productName'], item['price'], item['sales'], item['shopName']))
        


def getSourceByRequests(url):
    r = requests.get(url)
    source = r.text
    with open('source.txt', 'w', encoding='utf-8') as f:
        f.write(source)
    return source


def getSourceBySelenium(url):
    driver = webdriver.PhantomJS()
    # driver = webdriver.Chrome()
    driver.get(url)
    pageSource = driver.page_source
    driver.quit()
    with open('source.txt', 'w', encoding='utf-8') as f:
        f.write(pageSource)
    print('SourceCode Saved.')
    return pageSource


def getJDProductData(pageSource):
    productList = []
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
        productList.append(productDict)
    now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    resultDict = {
        "timestamp": time.localtime(),
        "time": now,
        "productList": productList,
    }
    return resultDict


def saveData(resultDict):
    timestamp = resultDict['timestamp']
    now = resultDict['now']
    for 
    with open(timestamp, 'w', encoding='utf-8'):



if __name__ == "__main__":
    main()