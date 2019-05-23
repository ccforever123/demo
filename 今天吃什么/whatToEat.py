# 菜单自动生成器
import requests
import random
import re

def main():
    hun = ['鸡肉', '牛肉', '排骨', '五花肉', '瘦肉', '鸡蛋', '鱼'] # 荤菜种类
    su = ['青菜', '胡萝卜', '黄瓜', '豆芽', '土豆', '花菜']  # 素材种类
    hunNum = '1'    # 荤菜数量
    suNum = '0' # 素菜数量
    score = '8.0'   # 定义评分低于指定分数的菜单不被选择
    noNeed = ['早餐', '炸']   # 屏蔽关键词
    keywordsHun = random.sample(hun, int(hunNum))
    keywordsSu = random.sample(su, int(suNum))
    keywords = keywordsHun + keywordsSu
    print('·· 您选择了{}荤{}素哦~'.format(hunNum, suNum))
    print('-> 我帮您选择了: {}'.format(keywords))
    menuList = []
    for keyword in keywords:
        search_nemu(menuList, keyword, score, noNeed)


def search_nemu(menuList, keyword, score='8.0', noNeed=[]):
    # 搜索下厨房：http://m.xiachufang.com/search/?keyword=x
    url = 'http://m.xiachufang.com/search/?keyword=' + keyword
    keywordSource = get_source(url) # 返回搜索结果源代码
    # selectMenu = [url, name, menuScore]
    selectMenu = read_source(keywordSource, score, noNeed)   # 返回下厨房对应食材的搜索首页的高于score分值的数据，并随机选择一条
    # 查看详细做法
    menuUrl = 'http://m.xiachufang.com' + selectMenu[0]
    menuSource = get_source(menuUrl)    # 返回选择菜单步骤页面源代码
    menuUrl = 'http://m.xiachufang.com' + selectMenu[0]
    menuSource = get_source(menuUrl)  # 返回选择菜单步骤页面源代码
    menuDict = get_menu_steps_m(menuSource, selectMenu[2])  # 获取原材料和步骤
    if menuDict == False:
        menuUrl = 'http://www.xiachufang.com' + selectMenu[0]
        menuSource = get_source(menuUrl)    # 返回选择菜单步骤页面源代码
        menuDict = get_menu_steps_w(menuSource, selectMenu[2])  # 获取原材料和步骤
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


def get_menu_steps_m(source, score):
    try:
        regTitle = re.findall(r'width=\"320\" height=\"260\" alt=\"(.*?)的做法\"', source, re.S)[0]
        regUrl = re.findall(r'rel=\"canonical\" href=\"(.*?)\">', source)[0]
        regPlain = re.compile(r'class=\"ing\" data-v-3a9590fe>(.*?)</a>', re.S)
        regPlainList = regPlain.findall(source)
        regSteps = re.compile(r'<div class=\"sub-title\" data-v-43643aae>(.*?)</div>.*?<p class=\"step-text\" data-v-43643aae>(.*?)</p>', re.S)
        regStepsList = regSteps.findall(source)
        menuDict = {
            "name": regTitle,
            "score": score,
            "url": regUrl,
            "plains": regPlainList,
            "steps": regStepsList
        }
        return menuDict
    except:
        return False


def get_menu_steps_w(source, score):
    print(source)
    regTitle = re.findall(r'<li itemprop=\"itemListElement\".*? class="active">.*?<span>(.*?)</span>', source, re.S)[0]
    regUrl = re.findall(r'rel=\"canonical\" href=\"(.*?)\">', source)[0]
    regPlain = re.compile(r'<tr itemprop="recipeIngredient">.*?<td class="name">.*?([\u4e00-\u9fa5]*?$)</td>', re.S)
    regPlainList = regPlain.findall(source)
    regSteps = re.compile(r'<p class=\"step-text\" data-v-43643aae>(.*?)</p>', re.S)
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
        for x in menuDict['plains']:
            print('{}'.format(x), end='\t')
        print('\n' + '-' * 31 + 'Steps' + '-' * 30)
        for step in menuDict['steps']:
            x_out = step[0].split('\n')[1].strip()
            y_out = step[1].split('\n')[1].strip()
            print('{} - {}'.format(x_out, y_out))
        print('☆★'*20 + '\n'*2)


if __name__ == '__main__':
    main()




