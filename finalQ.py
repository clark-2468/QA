#code for rules first
#constant
no_of_teams=3
no_of_players_per_team=3
no_of_boards= no_of_players_per_team
letters= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def load_opponents():
    


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

    def __str__(self):
        return f"{self.name}({self.team})"
        

all_players=[]
all_objects=[]
file_handle= open("opponents.txt", "r")
    
opponents_for_this_player=[]
for team_counter in range (1, no_of_teams+1):
    
    teamname= letters[team_counter-1]
    for player_counter in range (1, no_of_players_per_team+1):
        handle= teamname+str(player_counter)
        all_players.append(handle)

        read1= file_handle.readlines()
        oppo1= read1[2:4]
        opponents_for_this_player[0]= oppo1
        oppo2= read1[4:6]
        opponents_for_this_player[1]= oppo2
        oppo3= read1[6:8]
        opponents_for_this_player[2]= oppo3
        

        p1= Player(name=handle, team=teamname, opponents=opponents_for_this_player)
        all_objects.append(p1)


print(all_players)
print(all_objects)

p2= all_objects[1]
print(p2.team)

#all the players are kept in the basement
#rules

def rule1(player_id):
    rule1= True
    #convert player_id to index in the list named all_objects
    index_in_list= all_players.index(player_id)
    #Nobody may play the same opponent twice, nor twice against opponents from the same team
    #just check team
    team_played=[]
    for countingoppo in range (3):
        oppo=all_objects[index_in_list].opponents[countingoppo]
        team_played.append(oppo.team)
    if team_played[0]==team_played[1] or team_played[0]==team_played[2] or team_played[1]==team_played[2]:
        rule1=False
    
    return rule1

    #three rounds, three opponents




        
    
