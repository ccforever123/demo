# 生成球队球员数据
import random
from genName import randomName

def main():
    teamName = ''
    playerCount = 1
    genTeamPlayers(teamName, playerCount) # players is all the team players-info list


def genTeamPlayers(teamName, playerCount):
    count = 1
    position = ['defend', 'midfield', 'forward']  # D 防守球员，M 中场球员， A 进攻球员
    players = []    # 初始化球员列表
    while True:
        gkData = genGoalKeeperData(count)
        players.append(gkData)
        count += 1
        if count > 3:    # 生成3个守门员数据后退出循环
            break
    while True:
        playerData = genSinglePlayerData(count)      # 生成球员数据playerData
        players.append(playerData)  # 将生成的球员数据加入球员列表players中
        count += 1
        if count > playerCount:    # 生成playerCount个球员数据后退出循环
            break
    return players


def genGoalKeeperData(count):
    playerData = {
        "playerNumber": count,
        "name": randomName(),
        "birth": '{}.{}'.format(random.randint(1980, 2000), random.randint(1, 12)),
        "national": 'China',
        "ability": {
            "goalkeeper": random.randint(15, 20),
            "defend": random.randint(1, 10),
            "setup": random.randint(1, 10),
            "wing": random.randint(1, 10),
            "pass": random.randint(1, 10),
            "shoot": random.randint(1, 10),
            "freekick": random.randint(1, 15),
            "teamwork": random.random(),
        },
        "stamina": random.randint(1, 20),
        "state": random.randint(1, 20),
    }
    print(playerData)
    return playerData


def genSinglePlayerData(count):
    playerData = {
        "playerNumber": count,
        "name": randomName(),
        "birth": '{}.{}'.format(random.randint(1980, 2000), random.randint(1, 12)),
        "national": 'China',
        "ability": {
            "goalkeeper": random.randint(1, 10),    # 守门能力
            "defend": random.randint(1, 20),    # 防守能力
            "setup": random.randint(1, 20), # 组织进攻能力
            "dribble": random.randint(1, 20),  # 盘带能力
            "pass": random.randint(1, 20),  # 传球能力
            "shoot": random.randint(1, 20), # 射门能力
            "freekick": random.randint(1, 20),  # 任意球能力
            "teamwork": random.random(),    # 团队合作概率，[0,1]
        },
        "stamina": random.randint(1, 20),   # 体能，表达球场覆盖范围
        "state": random.randint(1, 20), # 状态，表达能力加成，暂未使用
    }
    # maxPosition = max(zip(playerData["Ability"].values(), playerData["Ability"].keys()))# 获取位置数据最大值
    # playerData["Position"] = maxPosition[1]
    print(playerData)
    return playerData



if __name__ == '__main__':
    main()