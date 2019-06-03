from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--headless')
import re
import requests
import time



def main():
    keywords = input('请输入关键词：')
    searchDict = {
        "jd": 'https://so.m.jd.com/ware/search.action?keyword={}'.format(keywords),
        "suning": 'https://m.suning.com/search/{}/'.format(keywords),
        'taobao': 'https://ai.taobao.com/search/index.htm?pid=mm_10011550_0_0&unid=&source_id=search&key={}&b=sousuo_ssk&clk1=&prepvid=200_11.226.222.17_112680_1559266230975'.format(keywords),
    }
    startSearch(keywords, searchDict)


def startSearch(keywords, searchDict):
    timestamp = int(time.time())
    now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    resultDict = {
            "timestamp": timestamp,
            "time": now,
            "productList": [],
        }
    for urlTitle in searchDict:
        url = searchDict[urlTitle]
        # pageSource = getSourceByRequests(url)
        if urlTitle == 'jd':
            print('\nSearching @ jd.com')
            pageSource = getSourceByRequests(url)
            resultDict = getJDProductData(pageSource, resultDict)
            print('JD Data Saved')
        elif urlTitle == 'suning':
            print('\nSearching @ suning.com')
            pageSource = getSourceBySelenium(url)
            resultDict = getSuningProductData(pageSource, resultDict)
            print('Suning Data Saved')
        elif urlTitle == 'taobao':
            print('\nSearching @ taobao.com')
            pageSource = getSourceByRequests(url)
            resultDict = getTaobaoProductData(pageSource, resultDict)
            print('Taobao Data Saved')
    saveData(resultDict, timestamp, keywords)


def getSourceByRequests(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36"
    }
    r = requests.get(url, headers=headers)
    source = r.text
    with open('source.html', 'w', encoding='utf-8') as f:
        f.write(source)
    print('SourceCode Saved.')
    return source


def getSourceBySelenium(url):
    # driver = webdriver.PhantomJS()
    driver = webdriver.Chrome(chrome_options = chrome_options)
    driver.get(url)
    pageSource = driver.page_source
    driver.quit()
    with open('source.html', 'w', encoding='utf-8') as f:
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
            "shopName": '京东-' + shopName
        }
        resultDict['productList'].append(productDict)
        print('{}\t{}\t{}\t{}'.format(productDict['productName'], productDict['price'], productDict['sales'], productDict['shopName']))
    return resultDict


def getSuningProductData(pageSource, resultDict):
    reg_product = re.compile(r'class=\"name\">(.*?)</p>.*?￥<strong>(.*?)</strong>(\..*?)</em>', re.S)
    products = reg_product.findall(pageSource)
    for productName, price0, price1 in products:
        productDict = {
            "productName": productName,
            "price": price0 + price1,
            "sales": '',
            "shopName": '苏宁店铺'
        }
        resultDict['productList'].append(productDict)
        print('{}\t{}\t{}\t{}'.format(productDict['productName'], productDict['price'], productDict['sales'], productDict['shopName']))
    return resultDict


def getTaobaoProductData(pageSource, resultDict):
    reg_product = re.compile(r'\"isTmall\":\"(.*?)\".*?\"sell\":\"(.*?)\",\"redKey.*?\"title\":\"(.*?)\".*?\"wangWangId\":\"(.*?)\",\"goodsPrice\":\"(.*?)\"')
    products = reg_product.findall(pageSource)
    for isTmall, sell, productName, shopName, price in products:
        if isTmall == '1':
            shopName = '天猫-' + shopName
        else:
            shopName = '淘宝' + shopName
        price0 = price[:-2]
        price1 = price[-2:]
        productDict = {
            "productName": productName,
            "price": price0 + '.' + price1,
            "sales": sell,
            "shopName": shopName
        }
        resultDict['productList'].append(productDict)
        print('{}\t{}\t{}\t{}'.format(productDict['productName'], productDict['price'], productDict['sales'], productDict['shopName']))
    return resultDict


def saveData(resultDict, timestamp, keywords):
    now = resultDict['time']
    text = '时间,产品名称,价格,销量,店铺\n'
    with open('{}-{}.csv'.format(keywords, timestamp), 'w', encoding='gbk') as f:
            f.write(text)
    for product in resultDict['productList']:
        productName = product['productName']
        price = product['price']
        sales = product['sales']
        shopName = product['shopName']
        text = '{},{},{},{},{}\n'.format(now, productName, price, sales, shopName)
        with open('{}-{}.csv'.format(keywords, timestamp), 'a', encoding='gbk') as f:
            f.write(text)


if __name__ == "__main__":
    main()