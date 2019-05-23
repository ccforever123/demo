# 生成球队球员数据
import random
from genName import randomName

def main():
    teamName = ''
    playerCount = 1
    players = genTeamPlayers(teamName, playerCount)


def genTeamPlayers(teamName, playerCount):
    position = ['D', 'M', 'A']
    players = []
    gk = genGKData()
    players.append(gk)
    for i in range(playerCount):
        playerData = genSinglePlayer(position)
        players.append(playerData)
    return players


def genGKData():
    playerData = {
        "Name": randomName(),
        "Birth": '{}.{}'.format(random.randint(1980, 2000), random.randint(1, 12)),
        "National": 'China',
        "Ability": {
            "G": random.randint(15, 20),
            "D": random.randint(1, 10),
            "M": random.randint(1, 10),
            "A": random.randint(1, 10),
        },
        "Position": 'G'
    }
    print(playerData)
    return playerData


def genSinglePlayer(position):
    playerData = {
        "Name": randomName(),
        "Birth": '{}.{}'.format(random.randint(1980, 2000), random.randint(1, 12)),
        "National": 'China',
        "Ability": {
            "G": random.randint(1, 10),
            "D": random.randint(1, 20),
            "M": random.randint(1, 20),
            "A": random.randint(1, 20),
        }
    }
    maxPosition = max(zip(playerData["Ability"].values(), playerData["Ability"].keys()))# 获取位置数据最大值
    playerData["Position"] = maxPosition[1]
    print(playerData)
    return playerData



if __name__ == '__main__':
    main()