#looking to qualify for "exceeds expectations" grade. 
import copy
from constants import PLAYERS
from constants import TEAMS

GREETING = 'BASKETBALL TEAM STATS TOOL\n'

players = copy.deepcopy(PLAYERS)
teams = copy.deepcopy(TEAMS)

max_players = len(players)/len(teams)
exp_players = []
nexp_players = []

panthers = []
bandits = []
warriors = []

       
squads = [panthers, bandits, warriors]
num_teams= len(squads)             
            
def balance_teams(players):
    for player in players:
        experience = player['experience']
       
        
        if experience == 'YES':
            exp_players.append(player)
            
        else:
            nexp_players.append(player)  


def balance_exp(exp_lists):
    for num in range(len(exp_lists)):
        squads[num % num_teams].append(exp_lists[num])
            
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
                exp_count = 0
                height = []
                for players in panthers:
                    if players['experience']== True:
                        exp_count += 1
                    height.append(players['height'])
                nexp_count = (members - exp_count)
                average_height = (round(sum(height)/members)) 
                
                print('\nTEAM: {} Stats\n--------------------\nTotal Players: {}\nExperienced Players: {}\nNon-experienced Players: {}\nAverage Height: {} inches\n\n'.format(team,members,exp_count,nexp_count, average_height))
                print(pretty_data(*panthers))
               
            elif team_sel.lower() == "b":
                team = "Bandits"
                members = len(bandits) 
                exp_count = 0
                height = []
                for players in bandits:
                    if players['experience']== True:
                        exp_count += 1
                    height.append(players['height'])
                nexp_count = (members - exp_count)
                average_height = (round(sum(height)/members)) 
                
                print('\nTEAM: {} Stats\n--------------------\nTotal Players: {}\nExperienced Players: {}\nNon-experienced Players: {}\nAverage Height: {} inches\n\n'.format(team,members,exp_count,nexp_count, average_height))
                print(pretty_data(*bandits))
            
            elif team_sel.lower() == "c":
                team = "Warriors"
                members = len(warriors)
                exp_count = 0
                height = []
                for players in warriors:
                    if players['experience']== True:
                        exp_count += 1
                    height.append(players['height'])
                nexp_count = (members - exp_count)
                average_height = (round(sum(height)/members)) 
                
                print('\nTEAM: {} Stats\n--------------------\nTotal Players: {}\nExperienced Players: {}\nNon-experienced Players: {}\nAverage Height: {} inches\n\n'.format(team,members,exp_count,nexp_count, average_height))
                print(pretty_data(*warriors))
                
        else:
            raise ValueError
      
    except ValueError as err:
        print("\nInvalid input.Please choose either A, B or C\n")     

def pretty_data(*team, sep = ','):
    names = []
    parents = []
    for player in team:        
        names.append(player['name'])
        parents.append(player['guardians'])
    print(f"Player's Names:\n {', '.join(names)}\n\nGuardians:\n {', '.join(parents)}\n")
    dis_options()
        
       
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
                
        for player in players:
            player['guardians'] = ', '.join(player['guardians'].split(' and '))
            

        
    print(GREETING.upper())
    print('-----MENU-----\n')
    balance_teams(players)
    balance_exp(exp_players)
    balance_exp(nexp_players)
    clean_data()
    dis_options()
   
   
    
