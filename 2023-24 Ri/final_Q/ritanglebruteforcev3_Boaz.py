import main as m
import time
import random
import math

def check(n,b,raw_data):
    timetable, teams=m.unpack_data(raw_data) #unpacks the text document and puts them into two arrays- timetable and teams
    #timetable: [round][match][player]
    #teams:[round]{team}{player}-match
    checks=False
    total_detriment=-10
    if(m.check_all_players(timetable,teams,n,b)): #check if all the players and teams are there
        if(m.rule_one(timetable,teams)):
            if(m.rule_two(timetable,teams)):
                if(m.rule_three(timetable,teams,n,b)):
                    if(m.rule_four(timetable,teams,b)):
                        if(m.rule_five(timetable,teams)):
                            if(m.rule_six(timetable,teams,n,b)):
                                if(m.rule_seven(timetable,teams)):
                                    if(m.rule_eight(timetable,teams)):
                                        if(m.rule_nine(timetable,teams,n)):
                                            checks=True
                                        else:
                                            total_detriment=-1
                                    else:
                                        total_detriment=-2
                                else:
                                    total_detriment=-3
                            else:
                                total_detriment=-4
                        else:
                            total_detriment=-5
                    else:
                        total_detriment=-6
                else:
                    total_detriment=-7
            else:
                total_detriment=-8
        else:
            total_detriment=-9
    
    if checks:
        detriment_X=m.calc_detriment_X(timetable,teams,n)
        detriment_Y=m.calc_detriment_Y(timetable,teams,n)
        detriment_Z=m.calc_detriment_Z(timetable,teams,n,b)
        total_detriment=detriment_X+detriment_Y+detriment_Z
    
        print("X Detriment: "+str(detriment_X))
        print("Y Detriment: "+str(detriment_Y))
        print("Z Detriment: "+str(detriment_Z))
    print("Total Detriment: "+str(total_detriment))
    return total_detriment

def create_random(n,b,r):
    raw_data=[]
    random.seed(time.time())#fully random
    for i in range(r):
        raw_data.append("#")
        if b%2==0:
            for x in range(1,b+1):
                poss_teams=list(range(n))
                for y in range(int(n/2)):
                    player_one=chr(poss_teams.pop(random.randrange(n-2*y))+65)+str(x)
                    player_two=chr(poss_teams.pop(random.randrange(n-2*y-1))+65)+str(x)
                    raw_data.append(player_one+" "+player_two)
        else:
            pass
    return raw_data

def create_semi_random(n,b,r):
    raw_data=[]
    random.seed(time.time())#fully random
    board_wise=[]#board,round,match
    record={}#{myteam}{team}-times
    isbad=True
    isbadsing=True
    while(isbad):
        board_wise=[]
        record={}#to fulfill rule 3
        for x in range(n):
            record[str(x)]=[]
            for y in range(n):
                if x!=y:
                    record[str(x)].append(0)
                else:
                    record[str(x)].append(r*b+1)
        if b%2==0:
            isbadsing=True
            for x in range(1,b+1):
                poss_teams=list(range(n))
                board_wise.append([])
                forbidden_teams={}#to fulfill rule 1
                for team_number in poss_teams:
                    forbidden_teams[str(team_number)]=[team_number]
                if isbadsing:
                    for i in range(r):
                        board_wise[-1].append([])
                        poss_teams=list(range(n))
                        holder=[]
                        if isbadsing:
                            for y in range(int(n/2)):
                                player_one=poss_teams.pop(random.randrange(len(poss_teams)))
                                for z in range(len(forbidden_teams[str(player_one)])):#removes teams that have come before
                                    if forbidden_teams[str(player_one)][z] in poss_teams:
                                        poss_teams.remove(forbidden_teams[str(player_one)][z])
                                        holder.append(forbidden_teams[str(player_one)][z])
                                if poss_teams:
                                    for p in range(n):
                                        if (p in poss_teams): 
                                            if record[str(x)][p]>=math.ceil(r*b/(n-1)):
                                                poss_teams.remove(p)
                                                holder.append(p)
                                            else:
                                                for q in range(2*math.floor(r*b/(n-1))-2*record[str(x)][p]):
                                                    poss_teams.append(p)
                                    if not poss_teams:
                                        isbadsing=False
                                        print("uhoh")
                                        break
                                        poss_teams.append(player_one)
                                    player_two=poss_teams[random.randrange(len(poss_teams))]
                                    poss_teams=list(set(poss_teams))
                                    poss_teams.remove(player_two)
                                    forbidden_teams[str(player_one)].append(player_two)
                                    forbidden_teams[str(player_two)].append(player_one)
                                    record[str(player_one)][player_two]+=1
                                    record[str(player_two)][player_one]+=1
                                    board_wise[-1][i].append(chr(player_one+65)+str(x)+" "+chr(player_two+65)+str(x))
                                else:
                                    isbadsing=False
                                    print("uhoh")
                                    break
                                    poss_teams.append(player_one)
                                poss_teams+=holder
                                holder=[]
                        else:
                            break
                else:
                    break
            if isbadsing:
                isbad=False
        else:
            pass
    for i in range(r):
        raw_data.append("#")
        for board in board_wise:
            raw_data+=board[i]
    return raw_data

def swap_colour(match):#what they are now
    white=match[0]
    black=match[1]
    return [black,white]

def change_colour(n,b,raw_data):
    record=[]#take a count of the total number of whites in each team- r*b/2 [team]-total number of whites
    team_record={}#a dictionary of arrays which counts the number of whites in a team {team}[player-1]-number of whites
    random.seed(time.time())#fully random
    timetable, teams=m.unpack_data(raw_data)
    ideal_team_whites=r*b/2
    ideal_whites=[math.floor(r/2),math.ceil(r/2)]
    whites=0
    
    for x in range(n):
        record.append(0)
        team_record[str(x)]=[]
        for y in range(b):
            team_record[str(x)].append(0)
    for team_name, team in teams[0].items():
        for player in team.keys():
            for round in range(len(teams)):#algorithm to find characteristics of player
                match=teams[round][team_name][player]
                if match[0]==player:#identifying if black or white
                    team_record[str(ord(team_name)-65)][int(player[1:])-1]+=1#is white, then put in team_record
    for x in range(n):
        for y in range(b):
            record[x]+=team_record[str(x)][y]
    tries=0
    isbad=True
    
    while isbad and tries<100:
        tries+=1
        more_tries=0
        isbad=False
        isbadsing=True
        while isbadsing and more_tries<10:
            more_tries+=1
            isbadsing=False
            x=random.randrange(n)#choosing a random team
            swapable_players=[]
            chosen_round=0
            if record[x]<ideal_team_whites:
                for y in range(b):
                    if team_record[str(x)][y]<r/2:
                        swapable_players.append(y)
                player_choice=swapable_players[random.randrange(len(swapable_players))]
                player_name=chr(x+65)+str(player_choice+1)
                passrounds=[]#not used here but if i change the program...
                chosen_round=0#the chosen round
                chosen_round_score=0#the score of the opponents team on the chosen round
                opponent_team=0
                opponent_team_whites=0
                for rounds in range(r):
                    if teams[rounds][chr(x+65)][player_name][1]==player_name:#if player is black
                        if teams[rounds][chr(x+65)][player_name][0][1:]==str(player_choice+1):#if no float
                            opponent_team=ord(teams[rounds][chr(x+65)][player_name][0][0])-65#team of the opponent
                            if team_record[str(opponent_team)][player_choice]>r/2 or chosen_round==0:
                                passrounds.append(rounds)
                                opponent_team_whites=record[opponent_team]#score of the opponents team
                                if opponent_team_whites>chosen_round_score:
                                    chosen_round_score=opponent_team_whites
                                    chosen_round=rounds
                opponent_team=ord(teams[chosen_round][chr(x+65)][player_name][0][0])-65
                                    
                add_on=1
                match=teams[chosen_round][chr(x+65)][player_name]
                
                record[x]+=add_on
                record[opponent_team]-=add_on
                team_record[str(x)][player_choice]+=add_on
                team_record[str(opponent_team)][player_choice]-=add_on
                teams[chosen_round][chr(x+65)][player_name]=swap_colour(match)
                
                teams[chosen_round][chr(opponent_team+65)][chr(opponent_team+65)+str(player_choice+1)]=list(teams[chosen_round][chr(x+65)][player_name])#does the swapping
            for x in range(n):
                if record[x]!=ideal_team_whites:
                    isbadsing=True
                        
            
        for y in range(n):#checks every player for good black and white
            for z in range(b):#y is team, z is player-1
                while not (team_record[str(y)][z] in ideal_whites): #this code only works if round<4
                    team_name=chr(y+65)
                    round = random.randrange(r)
                    match=teams[round][team_name][team_name+str(z+1)]
                    if (ord(match[0][0])-65)==y:#finding the opponent
                        opponent=match[1]
                        player=match[0]
                    else:
                        opponent=match[0]
                        player=match[1]
                    
                    whites=team_record[str(y)][z]
                    add_on=0
                    if n%2==1:
                        if whites<min(ideal_whites) and opponent[1:]<=player[1:]:#if opponent is not upfloated
                            add_on=+1
                        elif whites>max(ideal_whites) and opponent[1:]>=player[1:]:#if opponent is not downfloated
                            add_on=-1
                    else:
                        if whites<min(ideal_whites):
                            add_on=+1
                        else:
                            add_on=-1
                    record[y]+=add_on
                    record[ord(opponent[0])-65]-=add_on
                    team_record[str(y)][z]+=add_on
                    team_record[str(ord(opponent[0])-65)][int(opponent[1:])-1]-=add_on
                    teams[round][team_name][player]=swap_colour(match)
                    teams[round][opponent[0]][opponent]=swap_colour(match)#does the swapping
        for x in range(n):
            if record[x]!=ideal_team_whites:
                isbad=True
    if isbad:
        print("colour fail")
        end()
    raw_data=[]
    round_number=0
    for round in teams:
        round_number+=1
        raw_data.append("#"+str(round_number))
        for x in range(b):
            for team_name, team in round.items():
                player_name=team_name+str(x+1)
                match=team[player_name][0]+" "+team[player_name][1]
                #print(match)
                if not match in raw_data:
                    raw_data.append(match)
    return raw_data

n=12
b=10
r=3
numberOfSuccess=0
success=1000
successnumber=0
x=0
total_detriment=-10
colour=True
raw_data=[]
original_raw_data=[]
success_raw_data=[]
if colour:
    with open("#1text.txt",'r') as text_file:
        original_raw_data = text_file.readlines()
while x<200:
    x+=1
    raw_data=list(original_raw_data)
    print(str(x)+": ",end="")
    if not colour:
        raw_data=create_random(n,b,r)
        total_detriment=check(n,b,raw_data)
    else:
        raw_data=change_colour(n,b,raw_data)
        total_detriment=check(n,b,raw_data)
    if total_detriment<success and total_detriment>-1:
        success=total_detriment
        successnumber=x
        success_raw_data=raw_data
    #if total_detriment>-1:
if total_detriment>-1:
    raw_data=success_raw_data
    big_string=""
    hashtags=0
    for pair in raw_data:
        if pair[0]!="#":
            big_string+=pair+"\n"
        else:
            big_string+="#"+str(hashtags)+"\n"
            hashtags+=1
    big_string+="Total Detriment:"+str(success)
    numberOfSuccess+=1
    file_name="1"+"text"+str(numberOfSuccess)+".txt"#creates a file for the successful run
    with open(file_name, "w") as text_file:
        text_file.write(big_string)
print(successnumber)
print(success)#10-output is the place where they failed
    
    
    
