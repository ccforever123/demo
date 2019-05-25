import random
import time

teamAName = '拉齐奥'
teamBName = '国际米兰'

def main():
    result = [0, 0]
    teamA = [[5, 5, 5],
             [5, 5, 5],
             [5, 4, 6],
             [3, 6, 6]]

    teamB = [[5, 5, 5],
             [4, 6, 5],
             [5, 4, 6],
             [3, 9, 3]]
    homeTeam = []
    for i in teamA:
        homeTeam.append([])
        for j in i:
            a = j + 1   # 主队加成
            homeTeam[-1].append(a)
    chance = random.randint(5, 10)
    mins = random.sample(range(1, 90), chance)
    mins.sort()
    print('===============比赛开始了，本场比赛是{} 对阵 {}==============='.format(teamAName, teamBName))
    for i in range(chance):
        print('·  第{}分钟，'.format(mins[i]))
        homeIndex, awayIndex = 2, 2
        while True:
            time.sleep(0.5)
            position = random.randint(0, 2)
            homeIndex, awayIndex = cmp(teamA, teamB, homeIndex, awayIndex, position)
            if homeIndex == 0:
                result = shoot(result, teamBName, teamA, teamB, homeIndex, awayIndex-1, position)
                break

            elif awayIndex == 0:
                result = shoot(result, teamAName, teamA, teamB, homeIndex-1, awayIndex, position)
                break
    print('===============比赛结束了，最终比分是{} {}:{} {}==============='.format(teamAName, result[0], result[1], teamBName))




def cmp(teamA, teamB, aIndex, bIndex, position):    # 比较场上对应球员能力值
    totalScore = teamA[aIndex][position] + teamB[bIndex][position]
    score = random.random()
    aPersent = teamA[aIndex][position]/totalScore
    if score < aPersent:
        aIndex += 1
        bIndex -= 1
        print('-> {} 得到了球，'.format(teamAName), end='')
    else:
        aIndex -= 1
        bIndex += 1
        print('-> {} 得到了球，'.format(teamBName), end='')
    print('目前球处于[{},{}]位置'.format(aIndex, bIndex))
    return aIndex, bIndex


def shoot(result, attackTeam, teamA, teamB, aIndex, bIndex, position):    # 射门结果
    totalScore = teamA[aIndex][position] + teamB[bIndex][position]
    score = random.random()
    aPersent = teamA[aIndex][position] / totalScore
    print('!  {}射门！！！'.format(attackTeam))
    if score < aPersent:
        aIndex += 1
        bIndex -= 1
    else:
        aIndex -= 1
        bIndex += 1
    if aIndex == -1:
        result[1] += 1
        print('★ ☆ ★ ☆ ★ ☆ {} 进球了！比分为{}:{} ★ ☆ ★ ☆ ★ ☆'.format(teamBName, result[0], result[1]))
        return result
    elif bIndex == -1:
        result[0] += 1
        print('★ ☆ ★ ☆ ★ ☆ {} 进球了！比分为{}:{} ★ ☆ ★ ☆ ★ ☆'.format(teamAName, result[0], result[1]))
        return result
    else:
        print('×  可惜啊！被守门员拦下了！')
    return result

if __name__ == '__main__':
    main()
