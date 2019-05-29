import requests
import re

def main():
    keyword = input('请输入关键词:')
    urlDict = {
        # "京东": 'https://so.m.jd.com/ware/search.action?keyword={}'.format(keyword),
        "苏宁": 'https://m.suning.com/search/{}/'.format(keyword),
    }
    for urlSource in urlDict:
        url = urlDict[urlSource]
        source = getSource(url)
        if urlSource == '京东':
            productList = getJdProductList(source)
            for item in productList:
                print('{}\t{}\t{}\t{}'.format(item['productName'], item['price'], item['sales'], item['shopName']))
        elif urlSource == '苏宁':
            productList = getSuningProductList(source)
        
def getSource(url):
    r = requests.get(url)
    source = r.text
    with open('source.txt', 'w', encoding='utf-8') as f:
        f.write(source)
    return source
    
def getJdProductList(source):
    newProductList = []
    reg_product = re.compile(r'<div class=\"search_prolist_title\".*?>(.*?)</div>.*?pri=\"(.*?)\"></em>.*?<span id="com_.*?rd=\"0-4-1\">(.*?)</span>条评价</span>.*?class=\"shop_name\">(.*?)</span></div>', re.S)
    productList = reg_product.findall(source)
    # print(productList)
    for product, price, sales, shopName in productList:
        productDict = {
            "productName": product.split('  ')[-1],
            "price": price,
            "sales": sales,
            "shopName": shopName
        }
        newProductList.append(productDict)
    return newProductList


def getSuningProductList(source):
    return

if __name__ == "__main__":
    main()