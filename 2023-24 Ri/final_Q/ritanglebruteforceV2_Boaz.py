import main as m
import time
import random

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

n=12
b=10
r=3
number=0
success=-11
for x in range(4000):
    print(str(x)+": ",end="")
    raw_data=create_random(n,b,r)
    total_detriment=check(n,b,raw_data)
    if total_detriment>success:
        success=total_detriment
    if total_detriment>-1:
        big_string=""
        hashtags=0
        for pair in raw_data:
            if pair[0]!="#":
                big_string+=pair+"\n"
            else:
                big_string+="#"+str(hashtags)+"\n"
                hashtags+=1
        big_string+="Total Detriment:"+str(total_detriment)
        number+=1
        file_name="1"+"text"+str(number)+".txt"#creates a file for the successful run
        with open(file_name, "a") as text_file:
            text_file.write(big_string)
print(success)#10-output is the place where they failed
    
    
    
