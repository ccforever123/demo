# 比赛模拟器
import os
import random
import json


def main():
    path = os.path.join(os.getcwd(), 'teams')
    for parents, dirnames, filenames in os.walk(path):
        if filenames != []:
            homeTeamName, awayTeamName = random.sample(filenames, 2)
            homeTeamFile = os.path.join(path, homeTeamName)
            awayTeamFile = os.path.join(path, awayTeamName)
            break
    homeTeamData = getTeamData(homeTeamFile)
    awayTeamData = getTeamData(awayTeamFile)
    print(homeTeamFile, awayTeamFile)
    formation = [4,4,2]
    getFieldAbility(homeTeamData, formation)


def getTeamData(teamFile):  # 读取球队数据文件
    with open(teamFile, 'r') as f:
        teamData = json.load(f)
    return teamData


def startMatch(homeTeamData, awayTeamData): # 开始比赛模拟
    ball = [1, 1]
    if roll() == 0:
        attackTeam = homeTeamData['name']
    else:
        attackTeam = awayTeamData['name']



def getFieldAbility(teamData, formation):  # 获取球队信息及阵型，并生成场上能力值， formation = [4, 4, 2]
    playerSelects = random.sample(teamData['players'][3:], 10)
    # print(playerSelects)
    firstDict = {
        "goalkeeper": random.sample(teamData['players'][:3], 1),
        "defenders": playerSelects[:formation[0]],
        "midfielders": playerSelects[formation[0]:(formation[0]+formation[1])],
        "forwards": playerSelects[(formation[0] + formation[1]):]
    }
    firstList = [firstDict['defenders'], firstDict['midfielders'], firstDict['forwards']]
    print('goalkeeper: {}'.format(firstDict['goalkeeper']))
    for i in firstList:
        print(i)


def roll():   # roll点决定球权
    rollResult = random.random()
    if rollResult < 0.5:
        return 0    # 主队持球
    else:
        return 1    # 客队持球


def pk(attackPlayer, defendPlayer):   # 球员对抗, place = [x, y]
    pass


def action(playerData): # 判断球员动作
    playerAction = random.random()
    if playerAction < playerData['ability']['teamwork']:
        doAction = 'pass'
    else:
        doAction = 'dribble'
    return doAction


if __name__ == "__main__":
    main()