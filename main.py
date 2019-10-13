import random

from TeamManager import TeamManager
from team import League, Team
from player import generate_player

def main():
    # set up our data
    # generate some players
    players = []
    for i in range(100):
        players.append(generate_player())

    # set up 5 teams
    teams = [
        Team('Chelsea'),
        Team('Man City'),
        Team('Arsenal'),
        Team('West Ham'),
        Team('Hull City'),
        Team('Swansea')
    ]

    for team in teams:
        # give them 11 starting players
        for player_num in range(11):
            selected_player = random.choice(players)
            team.players.append(selected_player)
            players.remove(selected_player)



    # we have a single league
    first_league = League('Premiership League', teams, players)

    print('Season begins')

    # creat a manager
    manager = TeamManager(random.choice(teams), first_league)

    for i in range(10):
        manager.manage()
        first_league.play_round()
    print('Season ends')
if __name__ == '__main__':
    main()