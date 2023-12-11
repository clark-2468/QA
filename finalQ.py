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
        self.rounds_upfloat=rounds_upfloat
        self.rounds_downfloat=rounds_downfloat
        self.white_count=0
        self.black_count=0

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
        




        p1= Player(name=handle, team=teamname, opponents=opponents_for_this_player, rounds_upfloat=read1[8], rounds_downfloat=read1[9])
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



def findindex(player_id):
    index_in_list= all_players.index(player_id)
    return index_in_list


#rules

def rule_for_individual(index_in_list):#rule_for_individual
    rule_for_individual= True
    #convert player_id to index in the list named all_objects
    
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
            rule_for_individual=False
            print("rule2 broken")
            break

    #rule 1 simplified    
    #print(team_played)
    if team_played[0]==team_played[1] or team_played[0]==team_played[2] or team_played[1]==team_played[2]:
        rule_for_individual=False
        print("rule1 broken")


    #rule5
    #No player shall have more than one up-float or more than one down-float.
    if len(obj1.rounds_upfloat)>1 or len(obj1.rounds_downfloat)>1:
        rule_for_individual=False
        print("rule5 broken")
    
    #rule8
    # The number of times a player is black shall differ by no more than 1 from the number of times a player is white.
    dif= abs(obj1.black_count-obj1.white_count)
    if dif>1:
        rule_for_individual=False
        print("rule8 broken")
    
    return rule_for_individual

   

def rule3():
    pass
    #wth

def rule4():
    pass
    #Among the players on any given board, there shall be no more than one up-float or down-float per round.

def rule6():
    pass
    
    
a=findindex("A1")
Vpass=rule_for_individual(a)
print(Vpass)

        
    
