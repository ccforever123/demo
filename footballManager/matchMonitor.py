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
    homeLineup = getFieldAbility(homeTeamData)  # 获取球队信息及阵型，并生成场上能力值， formation默认 = [4, 4, 2]
    awayLineup = getFieldAbility(awayTeamData)  # 获取球队信息及阵型，并生成场上能力值， formation默认 = [4, 4, 2]
    lineups = [homeLineup, awayLineup]
    startMatch(lineups)


def getTeamData(teamFile):  # 读取球队数据文件
    with open(teamFile, 'r') as f:
        teamData = json.load(f)
    return teamData


def startMatch(lineups): # 开始比赛模拟
    # 随机生成机会次数，及机会分布的分钟数
    chances, minuteList = getChances(10, 20)
    # 开始机会循环
    for chance in range(chances):
        #初始化球的位置[1, 1]，球场宽度为[3, 4]， 球门位于y轴中心，两只球队分列左右两侧，主场在左，客场在右
        minute = minuteList[chance] # 当前机会所在分钟数
        ballx = 1 # 初始化球场x轴位置
        bally = 1 # 初始化球场y轴位置
        # roll点判断球权
        rollResult = roll() # 获取roll点结果
        if rollResult == 0:
            ballMove = 1
        else:
            ballMove = -1
        attackTeamData = lineups[rollResult]    # 判断进攻球队
        defendTeamData = lineups[1 - rollResult]    # 判断防守球队
        attackTeamName = attackTeamData['name'] # 进攻球队名称
        attackPlayerData = attackTeamData['players'][ballx][bally]  # 定位进攻球员
        defendPlayerData = defendTeamData['player'][ballx][bally] # 定位防守球员
        print('-> {attackTeamName} {attackTeamPlayerName} 拿到了球，他面对 {defendPlayerName} 的防守'.format(attackTeamName, attackPlayerData['name'], defendPlayerData['name']))
        faceGoalkeeper = 0
        while True: # 执行场上循环
            # 如果前方已经没有防守队员，则进行射门判断
            if faceGoalkeeper == 1:
                pass
            else:
                # 否则，判断进攻球员动作
                doAction = action(attackPlayerData)
                if doAction == 'dribble':   # 过人
                    dribbleResult = actionDribble(attackPlayerData, defendPlayerData)
                    if dribbleResult == 1:  # 如果过人成功，则重新进入新的一轮球员动作判断
                        ballx = ballx + ballMove
                        defendPlayerData = defendTeamData['player'][ballx][bally]
                        continue
                    else:   # 如果过人失败，则球权交换，并进行新的一轮球员动作判断
                        ballMove = 0 - (ballMove)
                        attackTeamData, defendTeamData = defendTeamData, attackTeamData   # 进攻防守方互换
                        attackPlayerData, defendPlayerData = defendPlayerData, attackPlayerData  # 进攻防守球员互换
                        continue
                elif doAction == 'pass':    # 如果是传球，则横穿给任意球员
                    # 选择传球位置
                    # 判断是否传球成功，根据两个防守球员的防守数值的平均数
                    # 更新球的位置及球员信息
                    pass
                else:   # 组织进攻
                    # 选择传给的球员位置
                    # 判断传球是否成功，，根据两个防守球员的防守数值的平均数
                    # 更新球的位置及球员信息
                    pass         


def getChances(chanceMin, chanceMax):
    chances = random.randint(10, 20)
    minuteList = random.sample([1, 95], chances)
    return chances, minuteList


def getFieldAbility(teamData, formation = [4,4,2]):  # 获取球队信息及阵型，并返回首发阵容名单， 暂定 formation 仅支持 [4, 4, 2]
    playerSelects = random.sample(teamData['players'][3:], 10)
    # print(playerSelects)
    lineupDict = {
        "goalkeeper": random.sample(teamData['players'][:3], 1),
        "defenders": playerSelects[:formation[0]],
        "midfielders": playerSelects[formation[0]:(formation[0]+formation[1])],
        "forwards": playerSelects[(formation[0] + formation[1]):]
    }
    lineupList = [lineupDict['defenders'], lineupDict['midfielders'], lineupDict['forwards']]
    print('goalkeeper: {}'.format(lineupDict['goalkeeper']))
    return lineupList


def roll():   # roll点决定球权
    rollResult = random.random()
    if rollResult < 0.5:
        return 0    # 主队持球
    else:
        return 1    # 客队持球


def action(playerData): # 判断球员动作
    playerAction = round(random.random(), 2) * 100   # roll点判断动作，保留2位小数
    if playerAction <= playerData['ability']['teamwork'][0]:    # 若roll点小于等于团队合作值0（过人）
        doAction = 'dribble'
    elif playerAction <= playerData['ability']['teamwork'][1]:    # 若roll点小于等于团队合作值1（横向传递）
        doAction = 'pass'
    else:   # 否则组织进攻（向前传递）
        doAction = 'setup'
    return doAction


def actionDribble(attackPlayer, defendPlayer):
    attackAbility = attackPlayer['ability']['dribble']
    defendAbility = defendPlayer['ability']['defend']
    totalAbility = attackAbility + defendAbility    # 总能力值
    getSuccessResult = random.randint(1, totalAbility)
    if getSuccessResult < attackAbility:
        return 1
    else:
        return 0


def actionPass(attackPlayerData):
    pass


def actionSetup(attackPlayerData):
    pass


def getAttackAndDefendTeam():


if __name__ == "__main__":
    main()