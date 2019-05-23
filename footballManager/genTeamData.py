# 生成球队数据
import json
from genTeamPlayer import genTeamPlayers


def main():
    teamNames = ['lazio', 'inter', 'milan', 'roma', 'juventus', 'torino']
    for teamName in teamNames:
        print('Start Gen {} data'.format(teamName))
        playerCount = 30
        players = genTeamPlayers(teamName, playerCount)
        teamData = {
            "players": players
        }
        with open('teams\\{}.json'.format(teamName), 'w', encoding='utf-8') as f:
            json.dump(teamData, f)


if __name__ == '__main__':
    main()