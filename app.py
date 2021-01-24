import random
from constants import PLAYERS
from constants import TEAMS

GREETING = 'BASKETBALL TEAM STATS TOOL\n'

players = PLAYERS.copy()
teams = TEAMS.copy()

print(GREETING.upper())


print('-----MENU-----\n')


max_players = len(players)/len(teams)
exp_players = []
nexp_players = []

panthers = []
bandits = []
warriors = []

            
            
def balance_teams(players):
    for player in players:
        experience = player['experience']
        player_name = player['name']
        
        if experience == 'YES':
            exp_players.append(player_name)
            
        else:
            nexp_players.append(player_name)  
       
    
def balance_exp(exp_players):
    for players in exp_players:
        
        if len(panthers) < max_players/2:
            panthers.append(players)
        elif len(bandits) < max_players/2:
            bandits.append(players)
        elif len(warriors) < max_players/2:
            warriors.append(players) 
         
        
def balance_nexp(nexp_players):
    for players in nexp_players:
        
        if len(panthers) < max_players:
            panthers.append(players)
        elif len(bandits) < max_players:
            bandits.append(players)
        elif len(warriors) < max_players:
            warriors.append(players)  
            
            
def dis_options():
    print('Here are your Choices: \n A) Display Team Stats \n B) Quit\n\n')
    while max_players > 0:
        try:
            activate = input('Enter an option: ')
            
            if activate.lower() == "a" or activate.lower() == "b":
                
                if activate.lower() == "a":
                    show_teams()
                
                elif activate.lower() == "b":
                    print('Thank you, come back for more basketball stats!')
                    exit()
            else:
                raise ValueError
        
        except ValueError as err:
            print("\nInvalid input.Please choose either A or B\n")
            

    
def show_teams():
    print('\nA)Panthers\n\nB)Bandits\n\nC)Warrirors\n\n')
    try:
        team_sel= input('Enter an option: ')
        if team_sel.lower() == "a" or team_sel.lower()=="b" or team_sel.lower() == "c":
            if team_sel.lower() == "a":
                team = "Panthers"
                members = len(panthers)
                print('\nTEAM: {} Stats\n--------------------\nTotal Players: {}\n'.format(team,members))
                team_list = print(*panthers,sep=', ')
               
            elif team_sel.lower() == "b":
                team = "Bandits"
                members = len(bandits)
                print('\nTEAM: {} Stats\n--------------------\nTotal Players: {}\n'.format(team,members))
                team_list = print(*bandits,sep=', ')
            
            elif team_sel.lower() == "c":
                team = "Warriors"
                members = len(warriors)
                print('\nTEAM: {} Stats\n--------------------\nTotal Players: {}\n'.format(team,members))
                team_list = print(*warriors,sep=', ')
                
        else:
            raise ValueError
      
    except ValueError as err:
        print("\nInvalid input.Please choose either A, B or C\n")     


        
if __name__ == '__main__':
    def clean_data():
        for player in players:
            if player['experience'].lower() == 'yes':
                player['experience'] = True
            else:
                player['experience'] = False
            
        for player in players:
            if player['height'] != int():
                player['height'] = int(player['height'].split()[0])
                
        for player in PLAYERS:
            player['guardians'] = player['guardians'].split(' and ')
    
      
    balance_teams(players)
    balance_exp(exp_players)
    balance_nexp(nexp_players)
    clean_data()
    dis_options()
    
    
