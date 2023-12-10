#code for rules first
#constant
no_of_teams=3
no_of_players_per_team=3
no_of_boards= no_of_players_per_team
letters= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def rule2(player1, player2):
    #players do not play against its team mate
    if player1[0]==player2[0]:
        return False
    
def flooring(input_number):
    #the largest integer less than or equal to x

    return int(input_number)

def ceiling(input_number):
    #the smallest integer greater than or equal to x

    return int(input_number)+1

class Player:
    def __init__(self, name, team, opponents):
        self.name = name
        self.team = team
        self.opponents = opponents

all_players=[]

for team_counter in range (1, no_of_teams+1):
    
    teamname= letters[team_counter-1]
    for player_counter in range (1, no_of_players_per_team+1):
        handle= teamname+str(player_counter)
        all_players.append(handle)


print(all_players)

#all the players are kept in the basement
basement = {name: Player(name=name) for name in all_players}

        
    
