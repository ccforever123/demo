# 比赛模拟器
import os
import random
import json
import time


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
    teamAgainst = [homeTeamData['teamName'], awayTeamData['teamName']]
    # print(homeTeamFile, awayTeamFile)
    homeLineup = getHomeFieldAbility(homeTeamData)  # 获取球队信息及阵型，并生成场上能力值， formation默认 = [4, 4, 2]
    awayLineup = getAwayFieldAbility(awayTeamData)  # 获取球队信息及阵型，并生成场上能力值， formation默认 = [4, 4, 2]
    lineups = [homeLineup, awayLineup]
    startMatch(lineups, teamAgainst)


def getTeamData(teamFile):  # 读取球队数据文件
    with open(teamFile, 'r') as f:
        teamData = json.load(f)
    return teamData


def startMatch(lineups, teamAgainst): # 开始比赛模拟
    score = [0, 0] # 初始化比分
    # 随机生成机会次数，及机会分布的分钟数
    chances, minuteList = getChances(10, 20)
    print('❤  ❤  ❤  比赛开始了，本场比赛是由 {} 主场对阵 {} ❤  ❤  ❤'.format(teamAgainst[0], teamAgainst[1]))
    # print('{}\n{}'.format(lineups[0], lineups[1]))
    # 开始机会循环
    for chance in range(chances):
        #初始化球的位置[2, 2]，球场宽度为[4, 4]，[门将, 后卫, 中场, 前锋]。 球门位于y轴中心，两只球队分列左右两侧，主场在左，客场在右
        minute = minuteList[chance] # 当前机会所在分钟数
        ballx = 2 # 初始化球场x轴位置
        bally = 2 # 初始化球场y轴位置
        # roll点判断球权
        rollResult = roll() # 获取roll点结果
        if rollResult == 0:
            ballMove = 1
        else:
            ballMove = -1
        attackTeamData = lineups[rollResult]    # 判断进攻球队阵容
        attackTeamIndex = rollResult   # 判断进攻球队是主队还是客队，0是主队，1是客队
        defendTeamData = lineups[1 - rollResult]    # 判断防守球队阵容
        attackPlayerData = attackTeamData[ballx][bally]  # 定位进攻球员
        defendPlayerData = defendTeamData[ballx][bally] # 定位防守球员
        print('==================== 第 {} 分钟 ===================='.format(minute))
        print('-> {} {} 拿到了球，他面对 {} 的防守'.format(teamAgainst[attackTeamIndex], attackPlayerData['name'], defendPlayerData['name']))
        faceGoalkeeper = 0
        while True: # 执行场上循环
            time.sleep(1)
            # 如果前方已经没有防守队员，则进行射门判断
            if faceGoalkeeper == 1:
                goalkeeperData = defendTeamData[0][0]
                shootResult = shoot(attackPlayerData, goalkeeperData)
                print('-> {} {} 直接面对门将了，他选择了射门！'.format(teamAgainst[attackTeamIndex], attackPlayerData['name']))
                if shootResult == 1:
                    ballControl = lineups.index(attackTeamData) # 判断射门方
                    score[ballControl] += 1
                    goalReason = [
                        '漂亮！这球直挂球门死角！',
                        '哇！漂亮的弧线球！',
                        '啊？啊！晃过门将！',
                        '好球！可惜打在了立柱上！诶？弹进了球门...',
                    ]   # 射门进球的原因
                    getGoalReason = random.sample(goalReason, 1)[0]
                    print('√  {}球进了！！！现在场上比分是 {} {} : {} {}'.format(getGoalReason, teamAgainst[0], score[0], score[1], teamAgainst[1]))
                    break
                else:
                    shootFailedReason = [
                        '哎呀，可惜了，球射偏了！',
                        '漂亮！门将出击将球没收了！',
                        '啊！啊，呸！这球打了飞机！',
                        '好球！可惜打在了立柱上！可惜了！',
                    ]   # 射门无进球的原因
                    print('×  {}'.format(random.sample(shootFailedReason, 1)[0]))
                    break
            else:   # 否则，判断进攻球员动作
                doAction = action(attackPlayerData)
                if doAction == 'dribble':   # 过人
                    print('-> {} {} 选择了过人...他面前的是{}'.format(teamAgainst[attackTeamIndex], attackPlayerData['name'], defendPlayerData['name']), end=' ')
                    dribbleResult = actionDribble(attackPlayerData, defendPlayerData)
                    if dribbleResult == 1:  # 如果过人成功，则重新进入新的一轮球员动作判断
                        print('漂亮的过人！')
                        ballx = ballx + ballMove
                        if ballx == 0 or ballx == 4:
                            faceGoalkeeper = 1
                            continue
                        # print('{}, {}'.format(ballx, bally))
                        try:
                            defendPlayerData = defendTeamData[ballx][bally]
                        except:
                            print('{} {} 向前带球'.format(teamAgainst[attackTeamIndex], attackPlayerData['name']))
                            ballx += ballMove
                        continue
                    else:   # 如果过人失败，则球权交换，并进行新的一轮球员动作判断
                        print('哎呀，过人被拦截了！')
                        ballMove = 0 - (ballMove)
                        attackTeamData, defendTeamData = defendTeamData, attackTeamData   # 进攻防守方互换
                        attackPlayerData, defendPlayerData = defendPlayerData, attackPlayerData  # 进攻防守球员互换
                        attackTeamIndex = abs(1 - attackTeamIndex)
                        print('-> {} {} 正在控球'.format(teamAgainst[attackTeamIndex], attackPlayerData['name']))
                        continue
                elif doAction == 'pass':    # 如果是传球，则横穿给任意球员
                    print('-> {} {} 他...'.format(teamAgainst[attackTeamIndex], attackPlayerData['name']), end=' ')
                    yLenth = len(attackTeamData[ballx])  # 获取足球所在x轴当前y轴的长度
                    # 选择传球位置
                    newbally = random.randint(0, yLenth-1)    # 获取新的bally位置
                    # 判断是否传球成功，根据两个防守球员的防守数值的平均数
                    passResult = actionPass(attackPlayerData, defendPlayerData, defendTeamData, ballx, newbally, doAction)
                    print('想要把球传给 {}'.format(attackPlayerData['name']), end=' ')
                    # 更新球的位置及球员信息
                    if passResult == 1: # 如果传球成功，则更新足球坐标，进入新一轮球员动作判断
                        bally = newbally
                        attackPlayerData = attackTeamData[ballx][bally]
                        defendPlayerData = defendTeamData[ballx][bally]
                        print('\n-> {} {} 接到了球，他正在观察。'.format(teamAgainst[attackTeamIndex], attackPlayerData['name']))
                        continue
                    else:   # 如果传球失败，则更新足球坐标，攻防方互换，进入新一轮球员动作判断
                        print('可惜，球没传过去。球被 {} 拦截了！'.format(defendPlayerData['name']))
                        bally = newbally
                        attackTeamData, defendTeamData = defendTeamData, attackTeamData   # 进攻防守方互换
                        attackPlayerData = attackTeamData[ballx][bally]
                        defendPlayerData = defendTeamData[ballx][bally]
                        attackTeamIndex = abs(1 - attackTeamIndex)
                        print('-> {} {} 控球'.format(teamAgainst[attackTeamIndex], attackPlayerData['name']))
                        continue
                else:   # 组织进攻
                    print('-> {} {} 打算长传交给前方的队友...'.format(teamAgainst[attackTeamIndex], attackPlayerData['name']), end=' ')
                    # 选择传给的球员位置
                    newballx = ballx + ballMove
                    if newballx <= 0 or newballx >= 4:
                        faceGoalkeeper = 1
                        print('哦不，这是假动作，他居然晃过后卫，直接面对门将了！')
                        continue
                    ballx = newballx
                    # print('newballx: {}'.format(newballx), end=' ')
                    yLenth = len(attackTeamData[ballx])  # 获取足球所在x轴当前y轴的长度
                    # print('yLenth: {}'.format(yLenth))
                    newbally = random.randint(0, yLenth-1)    # 获取新的bally位置
                    # 判断传球是否成功，，根据两个防守球员的防守数值的平均数
                    setupResult = actionPass(attackPlayerData, defendPlayerData, defendTeamData, ballx, newbally, doAction)
                    # 更新球的位置及球员信息
                    if setupResult == 1: # 如果传球成功，则更新足球坐标，进入新一轮球员动作判断
                        print('漂亮！，{} 一脚直传给到了'.format(attackPlayerData['name']), end=' ')
                        bally = newbally
                        attackPlayerData = attackTeamData[ballx][bally]
                        defendPlayerData = defendTeamData[ballx][bally]
                        print('{}'.format(attackPlayerData['name']))
                        continue
                    else:   # 如果传球失败，则更新足球坐标，攻防方互换，进入新一轮球员动作判断
                        bally = newbally
                        attackTeamData, defendTeamData = defendTeamData, attackTeamData   # 进攻防守方互换
                        attackPlayerData = attackTeamData[ballx][bally]
                        defendPlayerData = defendTeamData[ballx][bally]    
                        print('哎呀，可惜了。球被 {} 拦截了'.format(attackPlayerData['name']))   
                        attackTeamIndex = abs(1 - attackTeamIndex) 
                        continue
    print('▶  比赛结束了，最后比分是{} {}:{} {}'.format(teamAgainst[0], score[0], score[1], teamAgainst[1]))


def getChances(chanceMin, chanceMax):
    chances = random.randint(10, 20)
    minuteList = sorted(random.sample(range(1, 95), chances))
    return chances, minuteList


def getHomeFieldAbility(teamData, formation = [3,3,3]):  # 获取球队信息及阵型，并返回首发阵容名单， 暂定 formation 仅支持 [3, 3, 3]
    playerSelects = random.sample(teamData['players'][3:], 9)
    # print(playerSelects)
    lineupDict = {
        "goalkeeper": random.sample(teamData['players'][:3], 1),
        "defenders": playerSelects[:formation[0]],
        "midfielders": playerSelects[formation[0]:(formation[0]+formation[1])],
        "forwards": playerSelects[(formation[0] + formation[1]):]
    }
    lineupList = [lineupDict['goalkeeper'], lineupDict['defenders'], lineupDict['midfielders'], lineupDict['forwards']]
    return lineupList


def getAwayFieldAbility(teamData, formation = [3,3,3]):  # 获取球队信息及阵型，并返回首发阵容名单， 暂定 formation 仅支持 [3, 3, 3]
    playerSelects = random.sample(teamData['players'][3:], 9)
    # print(playerSelects)
    lineupDict = {
        "goalkeeper": random.sample(teamData['players'][:3], 1),
        "defenders": playerSelects[:formation[0]],
        "midfielders": playerSelects[formation[0]:(formation[0]+formation[1])],
        "forwards": playerSelects[(formation[0] + formation[1]):]
    }
    lineupList = [lineupDict['goalkeeper'], lineupDict['forwards'], lineupDict['midfielders'], lineupDict['defenders']]
    return lineupList


def roll():   # roll点决定球权
    rollResult = random.random()
    if rollResult < 0.5:
        return 0    # 主队持球
    else:
        return 1    # 客队持球


def action(playerData): # 判断球员动作
    playerAction = round(random.random(), 2) * 100   # roll点判断动作，保留2位小数
    # print(playerAction, playerData['ability']['teamwork'])
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


def actionPass(attackPlayerData, defendPlayerData, defendTeamData, ballx, newbally, doAction):
    passAbility = attackPlayerData['ability'][doAction]
    # print('ballx: {}, newbally: {}'.format(ballx, newbally))
    defendPlayer2Data = defendTeamData[ballx][newbally]
    defendAbility = int((defendPlayerData['ability']['defend'] + defendPlayer2Data['ability']['defend'])/2)
    totalAbility = passAbility + defendAbility  # 总能力值
    getPassResult = random.randint(1, totalAbility)
    if getPassResult < passAbility:
        return 1
    else:
        return 0


def actionSetup(attackPlayerData):
    pass


def shoot(attackPlayerData, goalkeeperData):
    shootAbility = attackPlayerData['ability']['shoot']
    goalkeeperAbility = goalkeeperData['ability']['goalkeeper']
    totalAbility = shootAbility + goalkeeperAbility
    getShootResult = random.randint(1, totalAbility) # 总能力值
    if getShootResult < shootAbility:
        return 1
    else:
        return 0


def getAttackAndDefendTeam():
    pass

if __name__ == "__main__":
    main()