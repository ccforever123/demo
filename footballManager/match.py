import random


def main():
    result = [0, 0]
    teamA = [[3,3,3], [4, 4, 4], [4, 5.5, 4], [4, 3, 3.5]]
    teamB = [[3,3,3], [4, 3, 4], [4, 6, 4], [4, 4, 3]]
    homeTeam = []
    for i in teamA:
        homeTeam.append([])
        for j in i:
            a = j + 1   # 主队加成
            homeTeam[-1].append(a)
    chance = random.randint(5, 10)
    for i in range(chance):
        homeIndex, awayIndex = 1, 1
        while True:
            position = random.randint(0, 2)
            homeIndex, awayIndex = cmp(homeTeam, teamB, homeIndex, awayIndex, position)
            if homeIndex == 0 or awayIndex == 0:
                result = shoot(result, homeTeam, teamB, homeIndex, awayIndex, position)
                break




def cmp(teamA, teamB, aIndex, bIndex, position):    # 比较场上对应球员能力值
    totalScore = teamA[aIndex][position] + teamB[bIndex][position]
    score = random.random()
    aPersent = teamA[aIndex][position]/totalScore
    if score < aPersent:
        aIndex += 1
        bIndex -= 1
    else:
        aIndex -= 1
        bIndex += 1
    print('{},{}'.format(aIndex, bIndex))
    return aIndex, bIndex


def shoot(result, teamA, teamB, aIndex, bIndex, position):    # 射门结果
    totalScore = teamA[aIndex][position] + teamB[bIndex][position]
    score = random.random()
    aPersent = teamA[aIndex][position] / totalScore
    if score < aPersent:
        aIndex += 1
        bIndex -= 1
    else:
        aIndex -= 1
        bIndex += 1
    if aIndex == -1:
        result[1] += 1
        print('进球了！比分为{}'.format(result))
        return result
    elif bIndex == -1:
        result[0] += 1
        print('进球了！比分为{}'.format(result))
        return result
    return result

if __name__ == '__main__':
    main()
