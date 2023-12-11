#code for rules first
#constant
no_of_teams=3
no_of_players_per_team=3
no_of_boards= no_of_players_per_team
letters= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


#two operations
    
def flooring(input_number):
    #the largest integer less than or equal to x

    return int(input_number)

def ceiling(input_number):
    #the smallest integer greater than or equal to x

    return int(input_number)+1




#the core class
class Player:
    def __init__(self, name, team, opponents,rounds_upfloat,rounds_downfloat):
        self.name = name
        self.team = team
        self.opponents = opponents
        self.rounds_upfloat=''
        self.rounds_downfloat=''

    #def __str__(self):
        #return f"{self.name}({self.team})"
        



#ini loading section
all_players=[]#name in Aa format
all_objects=[]#name in pointer format

file_handle= open("opponents.txt", "r")
    
opponents_for_this_player=['','','']
for team_counter in range (1, no_of_teams+1):
    
    teamname= letters[team_counter-1]
    for player_counter in range (1, no_of_players_per_team+1):
        handle= teamname+str(player_counter)
        all_players.append(handle)

        read1= file_handle.readline()

        print(read1)
        oppo1= read1[2:4]
        opponents_for_this_player[0]= oppo1
        oppo2= read1[4:6]
        opponents_for_this_player[1]= oppo2
        oppo3= read1[6:8]
        opponents_for_this_player[2]= oppo3
        print(opponents_for_this_player)
        
        rounds_upfloat=read1[8]
        rounds_downfloat=read1[9]

        print(rounds_upfloat)

        p1= Player(name=handle, team=teamname, opponents=opponents_for_this_player, rounds_upfloat=rounds_upfloat, rounds_downfloat=rounds_downfloat)
        all_objects.append(p1)

file_handle.close()




#debug prints
print(all_players)
print(all_objects)

testinghandle= all_objects[0]
print(testinghandle.opponents)
print(testinghandle.team)
print(testinghandle.name)
print(testinghandle.rounds_upfloat)
print(testinghandle.rounds_downfloat)






#rules

def rule12(player_id):
    rule12= True
    #convert player_id to index in the list named all_objects
    index_in_list= all_players.index(player_id)
    #Nobody may play the same opponent twice, nor twice against opponents from the same team
    #just check team
    team_played=[]
    for countingoppo in range (3):
        obj1=all_objects[index_in_list]
        oppo_played= obj1.opponents[countingoppo]
        print(oppo_played)

        team_played.append(oppo_played[0])
        #include rule 2 so no friendly fire
        if team_played==obj1.team:
            rule12=False
            break
    #print(team_played)
    if team_played[0]==team_played[1] or team_played[0]==team_played[2] or team_played[1]==team_played[2]:
        rule12=False
   
    
    return rule12

    #three rounds, three opponents

def rule3():
    pass
    #wth

def rule4():
    pass
    #Among the players on any given board, there shall be no more than one up-float or down-float per round.

def rule5():
    pass
    #No player shall play the same board number more than once.

Vpass=rule12("A1")
print(Vpass)

        
    
