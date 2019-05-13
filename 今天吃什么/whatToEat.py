# 菜单自动生成器
import requests
import random
import re

def main():
    hun = ['鸡肉', '牛肉', '排骨', '五花肉', '瘦肉', '鸡蛋', '鱼'] # 荤菜种类
    su = ['青菜', '胡萝卜', '黄瓜', '豆芽', '土豆', '花菜']  # 素材种类
    hunNum = '1'    # 荤菜数量
    suNum = '2' # 素菜数量
    score = '8.0'   # 定义评分低于指定分数的菜单不被选择
    noNeed = ['早餐', '炸']   # 屏蔽关键词
    keywordsHun = random.sample(hun, int(hunNum))
    keywordsSu = random.sample(su, int(suNum))
    keywords = keywordsHun + keywordsSu
    print('·· 您选择了{}荤{}素哦~'.format(hunNum, suNum))
    print('-> 我帮您选择了: {}'.format(keywords))
    menuList = []
    for keyword in keywords:
        # 搜索下厨房：http://m.xiachufang.com/search/?keyword=x
        url = 'http://m.xiachufang.com/search/?keyword=' + keyword
        keywordSource = get_source(url) # 返回搜索结果源代码
        # selectMenu = [url, name, menuScore]
        selectMenu = read_source(keywordSource, score, noNeed)   # 返回下厨房对应食材的搜索首页的高于score分值的数据，并随机选择一条
        # 查看详细做法
        menuUrl = 'http://m.xiachufang.com' + selectMenu[0]
        menuSource = get_source(menuUrl)    # 返回选择菜单步骤页面源代码
        menuDict = get_menu_steps(menuSource, selectMenu[2])  # 获取原材料和步骤
        menuList.append(menuDict)
    print_out(menuList) # 打印菜单


def get_source(url):
    r = requests.get(url)
    return r.text


def read_source(source, score, noNeed):
    menuList =[]
    regMenuText = re.compile(r'<a href=\"(/recipe.*?)\" class=\"recipe-96-horizon\".*?<header class=\"name font18\">(.*?)</header>.*?<div class=\"stat flex-1\">评分 <span>(.*?)</span>', re.S)
    regMenuList = regMenuText.findall(source)
    for i in regMenuList:
        if float(i[2]) >= float(score):
            for j in noNeed:
                if j not in i:
                    menuList.append(i)
    selectMenu = random.sample(menuList, 1)[0]
    return selectMenu


def get_menu_steps(source, score):
    regTitle = re.findall(r'<h1 class=\"plain\">(.*?)</h1>', source)[0]
    regUrl = re.findall(r'<link rel=\"canonical\" href=\"(.*?)\">', source)[0]
    regPlain = re.compile(r'<span class=\"ingredient\">(.*?)</span>.*?<span class=\"weight\">(.*?)</span>', re.S)
    regPlainList = regPlain.findall(source)
    regSteps = re.compile(r'<aside class=\"sub-title\">(.*?)</aside>.*?<p class=\"word-wrap\">(.*?)</p>', re.S)
    regStepsList = regSteps.findall(source)
    menuDict = {
        "name": regTitle,
        "score": score,
        "url": regUrl,
        "plains": regPlainList,
        "steps": regStepsList
    }
    return menuDict


def print_out(menuList):
    print('√  今天的菜单是: {}\n'.format(list(x['name'] for x in menuList)))
    for menuDict in menuList:
        print('☆★' * 20)
        print('-' * 31 + 'Name' + '-' * 31)
        print('{} - {} - {}'.format(menuDict['name'], menuDict['score'], menuDict['url']))
        print('-'*30 + 'Plains' + '-'*30)
        for x, y in menuDict['plains']:
            print('{} - {}'.format(x, y), end='\t')
        print('\n' + '-' * 31 + 'Steps' + '-' * 30)
        for x, y in menuDict['steps']:
            print('{} - {}'.format(x, y))
        print('☆★'*20 + '\n'*2)


if __name__ == '__main__':
    main()




