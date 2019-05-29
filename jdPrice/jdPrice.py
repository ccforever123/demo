import requests
import re

def main():
    keyword = input('请输入关键词:')
    urlList = [
        'https://so.m.jd.com/ware/search.action?keyword={}'.format(keyword),
    ]
    for url in urlList:
        source = getJdSource(url)
        print(source)
        getProductPriceList(source)



def getJdSource(url):
    r = requests.get(url)
    source = r.text
    return source


def getProductPriceList(source):
    newProductList = []
    reg_product = re.compile(r'<div class=\"search_prolist_title\".*?>(.*?)</div>.*?pri=\"(.*?)\"></em>.*?<span id="com_.*?rd=\"0-4-1\">(.*?)</span>条评价</span>.*?class=\"shop_name\">(.*?)</span>', re.S)
    productList = reg_product.findall(source)
    for product, price, sales, shopName in productList:
        productDict = {
            "productName": product.split(' ')[-1],
            "price": price,
            "sales": sales,
            "shopName": shopName
        }
        newProductList.append(productDict)
    print(newProductList)


if __name__ == "__main__":
    main()