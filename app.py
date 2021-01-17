import random
from constants import PLAYERS,TEAMS

players = PLAYERS.copy()
teams = TEAMS.copy()



num_of_players= len(players)
num_of_teams = len(teams)
max_players = num_of_players/num_of_teams
    

#if __name__ = '__main__':
    
def show_roster(roster_list):
    for player in roster_list:
        print(f" Name: {player['name']} \n Guardians: {player['guardians']} \n Experience: {player['experience']} \n Height: {player['height']}\n")
        
def balance_teams(team_list):
    for team in team_list:
        team_member = []
        if len(team_member) < max_players:
            team_member.append(players)
            print(team)
        
for player in players:
    if player['experience'].lower() == 'yes':
        player['experience'] = True
    else:
        player['experience'] = False
        
for player in players:
    if player['height'] != int():
        player['height'] = int(player['height'].split()[0])
     
     
show_roster(players)
balance_teams(teams)