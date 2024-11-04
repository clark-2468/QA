import math

def rule_one(timetable, teams):
    #Nobody may play the same opponent twice, nor twice against opponents from the same team.
    isCorrect=True
    problem=[]#player, round, clash round
    opponents=[]
    for team_name, team in teams[0].items():
        for player in team.keys():
            opponents=[]
            for round in range(len(teams)):
                match=teams[round][team_name][player]
                if match[0]==player:#finding the opponent
                    opponent=match[1]
                else:
                    opponent=match[0]
                for prev_opponent, prev_round in opponents:
                    if prev_opponent[0]==opponent[0]:
                        isCorrect=False
                        problem.append([player, round+1, prev_round+1])
                opponents.append([opponent, round])
                        
    if isCorrect:
        print("Rule One Passed")
    else:
        print("Rule One Failed")
        print(problem)
    
def rule_two(timetable, teams):
    #Nobody may play against a team-mate
    isCorrect=True
    problem=[]
    for round in timetable:
        for match in round:
            player_one=match[0]
            player_two=match[1]
            if player_one[0]==player_two[0]:
                isCorrect=False
                problem.append(player_one)
    if isCorrect:
        print("Rule Two Passed")
    else:
        print("Rule Two Failed")
        print(problem)

def rule_three(timetable, teams, n, b):
    #The number of times that each team plays each of the others shall be either 
    #floor(rb/(n-1)) or ceiling(rb/(n-1))
    isCorrect=True
    problem=[]#team, other team, times
    lowerbound=math.floor(len(teams)*b/(n-1))
    upperbound=math.ceil(len(teams)*b/(n-1))
    chart={}
    for team_name, team in teams[0].items():
        chart={}
        for x in range(n):
            chart[chr(x+65)]=0 #makes all of the teams blank
        for player in team.keys():
            for round in range(len(teams)):
                match=teams[round][team_name][player]
                if match[0]==player:#finding the opponent
                    opponent=match[1]
                else:
                    opponent=match[0]
                chart[opponent[0]]+=1
        for oppoteam_name, oppoteam in chart.items():
            if oppoteam!=upperbound and oppoteam!=lowerbound and oppoteam_name!=team_name:
                isCorrect=False
                problem.append([team_name, oppoteam_name, oppoteam])
    if isCorrect:
        print("Rule Three Passed")
    else:
        print("Rule Three Failed")
        print(problem)

def rule_four(timetable, teams, b):
    #Among the players on any given board, there shall be no more than one up-float or down-float per round.
    isCorrect=True
    problem=[]#board, round, floats
    floats=0
    for round in range(len(teams)):
        for board in range(1, b+1):
            floats=0
            for team_name, team in teams[round].items():
                player=team_name+str(board)
                match=team[player]
                if match[0]==player:#finding the opponent
                    opponent=match[1]
                else:
                    opponent=match[0]
                if opponent[1]!=player[1]:#identifying floats
                    floats+=1
            if floats>1:
                isCorrect=False
                problem.append([board, round, floats])
    if isCorrect:
        print("Rule Four Passed")
    else:
        print("Rule Four Failed")
        print(problem)

def rule_five(timetable, teams):
    #No player shall have more than one up-float or more than one down-float.
    isCorrect=True
    problem=[]#player, round, clash round
    floats=[]
    for team_name, team in teams[0].items():
        for player in team.keys():
            floats=[]
            for round in range(len(teams)):
                match=teams[round][team_name][player]
                if match[0]==player:#finding the opponent
                    opponent=match[1]
                else:
                    opponent=match[0]
                if opponent[1]!=player[1]:#identifying floats
                    floats.append([player, round])
                    if len(floats)>1:
                        isCorrect=False
                        problem.append([player, round+1, floats[-2][1]+1])
    if isCorrect:
        print("Rule Five Passed")
    else:
        print("Rule Five Failed")
        print(problem)

def rule_six(timetable, teams, n, b):
    #Over all the rounds taken together, no team shall have more than 2+floor(rb/2n) up-floats 
    #nor more than 2+floor(rb/2n) down-floats.
    isCorrect=True
    problem=[]#team, up-floats, down-floats
    up_floats=0
    down_floats=0
    limit=math.floor((len(teams)*b)/(2*n))
    for team_name, team in teams[0].items():
        up_floats=0
        down_floats=0
        for player in team.keys():
            for round in range(len(teams)):
                match=teams[round][team_name][player]
                if match[0]==player:#finding the opponent
                    opponent=match[1]
                else:
                    opponent=match[0]
                if opponent[1]<player[1]:#identifying upfloats
                    up_floats+=1
                elif opponent[1]>player[1]:#identifying downfloats
                    down_floats+=1
        if up_floats>limit or down_floats>limit:
            isCorrect=False
            problem.append([team_name, up_floats, down_floats])
    if isCorrect:
        print("Rule Six Passed")
    else:
        print("Rule Six Failed")
        print(problem)

def rule_seven(timetable, teams):
    #All up-floats shall have the white pieces.
    isCorrect=True
    problem=[]#player, round
    for team_name, team in teams[0].items():
        for player in team.keys():
            for round in range(len(teams)):
                match=teams[round][team_name][player]
                if match[0]==player:#finding the opponent
                    opponent=match[1]
                else:
                    opponent=match[0]#If they opponent has white
                    if opponent[1]<player[1]:#identifying upfloat
                        isCorrect=False
                        problem.append([player, round+1])
    if isCorrect:
        print("Rule Seven Passed")
    else:
        print("Rule Seven Failed")
        print(problem)

def rule_eight(timetable, teams):
    # The number of times a player is black shall differ by no more than 1 from the number of times a player is white.
    isCorrect=True
    problem=[]#player, difference (positive is white, negative is black)
    white_count=0
    black_count=0
    for team_name, team in teams[0].items():
        for player in team.keys():
            white_count=0
            black_count=0
            for round in range(len(teams)):#algorithm to find characteristics of player
                match=teams[round][team_name][player]
                if match[0]==player:#identifying if black or white
                    white_count+=1
                else:
                    black_count+=1
            difference=white_count-black_count
            if abs(difference)>1: #identifying if absolute difference>1
                isCorrect=False
                problem.append([player, difference])
    if isCorrect:
        print("Rule Eight Passed")
    else:
        print("Rule Eight Failed")
        print(problem)

def rule_nine(timetable, teams, n):
    #Over all the rounds taken together, the number of blacks for each team shall equal the number of whites.
    isCorrect=True
    problem=[]
    black_count=0
    white_count=0
    for x in range(n):
        team=chr(x+65)
        for round in range(len(teams)):
            for player_one, player_two in teams[round][team].values():
                if player_one[0]==team:
                    white_count+=1
                else:
                    black_count+=1
        if white_count != black_count:
            isCorrect=False
            problem.append(team)
            white_count,black_count=0,0
    if isCorrect:
        print("Rule Nine Passed")
    else:
        print("Rule Nine Failed")
        print(problem)

def unpack_data(text_name):
    text_file = open(text_name,'r')
    raw_data = text_file.readlines()
    timetable = []
    teams = []
    #if there is a #, it means new round
    for pair in raw_data:
        if pair[0] != "#":
            pair = pair.split('\n')[0] #removing the newline char
            newpair = pair.split()
            if len(newpair) != 2:
                print("Not formatted correctly, must have hashtag and must have only 2 players")
                end()
            newpair[0]=newpair[0][0].upper()+newpair[0][1]
            newpair[1]=newpair[1][0].upper()+newpair[1][1]
            timetable[-1].append(newpair)
            for i in range(2):
                if not teams[-1].get(newpair[i][0]):
                    teams[-1][newpair[i][0]]={}#making a new team is there isn't already one
                if not teams[-1][newpair[i][0]].get(newpair[i]):#checking for duplicates
                    teams[-1][newpair[i][0]][newpair[i]]=newpair
                else:
                    print("You have a duplicate of "+newpair[i])
        else:
            timetable.append([])
            teams.append({})
    return timetable, teams

def check_all_players(timetable,teams,n,b):
    for round in range(len(timetable)):
        if len(teams[round])>n*b/2: #seeing if the right number of players are there
            print("There are too many players in round: "+str(round+1))
            if len(teams[round].keys())>n:
                print("There are too many teams")
            for team in teams[round].keys():
                if len(teams[round][team].keys())>b:
                    print(team+" has too many players")
        elif len(timetable[round])<n*b/2:
            print("Not all the players in round: "+str(round+1)+" are there.")
            for team in teams[round].keys():
                for x in range(1, b+1):
                    if not teams[round][team].get(team+str(x)): #searching for the missing players
                        print(team+str(x)+" is missing")

def calc_detriment_X(timetable,teams,n):
    #In each round, the number of blacks for each team should be similar to the number of whites.
    detriment=0
    record={}#{team}{round}-difference
    white_count=0
    black_count=0
    for x in range(n):
        team=chr(x+65)
        record[team]={}
        for round in range(len(teams)):
            for player_one, player_two in teams[round][team].values():
                if player_one[0]==team:
                    white_count+=1
                else:
                    black_count+=1
            difference=abs(white_count-black_count)
            white_count=0
            black_count=0
            detriment+=difference#adding difference per team per round to total
            record[team][str(round+1)]=difference
    print("Detriment X: ",end="")
    print(record)
    return detriment

def calc_detriment_Y(timetable,teams,n):
    #Over all the rounds taken together, the number of up-floats for each team should be as close as possible to the number of down-floats.  
    detriment=0
    record={}#{team}-difference
    up_floats=0
    down_floats=0
    for team_name, team in teams[0].items():
        up_floats=0
        down_floats=0
        for player in team.keys():
            for round in range(len(teams)):
                match=teams[round][team_name][player]
                if match[0]==player:#finding the opponent
                    opponent=match[1]
                else:
                    opponent=match[0]
                if opponent[1]<player[1]:#identifying upfloats
                    up_floats+=1
                elif opponent[1]>player[1]:#identifying downfloats
                    down_floats+=1
        difference=abs(up_floats-down_floats)
        detriment+=difference#adding difference per team to total
        record[team_name]=difference
    print("Detriment Y: ",end="")
    print(record)
    return detriment

def calc_detriment_Z(timetable,teams,n,b):
    #For each team, the black games and white games should be evenly distributed down the team 
    #(i.e. it is undesirable for the higher boards to have a preponderance of whites and the lower boards to have a preponderance of blacks).
    detriment=0
    record={}#{team}-difference
    white_count=0
    multiplier=4/(len(teams)*b*(b+1))#making the multiplier(which is constant in the game)
    for x in range(n):
        team=chr(x+65)
        white_count=0
        for round in range(len(teams)):
            for player_one, player_two in teams[round][team].values():
                if player_one[0]==team:
                    white_count+=int(player_one[1])
        difference=abs(1-multiplier*white_count)
        detriment+=difference#adding difference per team per round to total
        record[team]=difference
    print("Detriment Z: ",end="")
    print(record)
    return detriment

def main(n, b, file):
    timetable, teams=unpack_data(file) #unpacks the text document and puts them into two arrays- timetable and teams
    #timetable: [round][match][player]
    #teams:[round]{team}{player}-match
    check_all_players(timetable,teams,n,b) #check if all the players and teams are there
    rule_one(timetable,teams)
    rule_two(timetable,teams)
    rule_three(timetable,teams,n,b)
    rule_four(timetable,teams,b)
    rule_five(timetable,teams)
    rule_six(timetable,teams,n,b)
    rule_seven(timetable,teams)
    rule_eight(timetable,teams)
    rule_nine(timetable,teams,n)
    
    detriment_X=calc_detriment_X(timetable,teams,n)
    detriment_Y=calc_detriment_Y(timetable,teams,n)
    detriment_Z=calc_detriment_Z(timetable,teams,n,b)
    
    print("X Detriment: "+str(detriment_X))
    print("Y Detriment: "+str(detriment_Y))
    print("Z Detriment: "+str(detriment_Z))
    print("Total Detriment: "+str(detriment_X+detriment_Y+detriment_Z))
    
    #print(timetable)
    #print(teams)
    print("success!")

if __name__ == "__main__":
    n = 6 #number of teams
    b = 4 #number of players
    file = "text.txt"
    main(
        n=n,
        b=b,
        file=file
    )