def detriment_calculator():
    pass

def rule_one():
    pass

def rule_two():
    pass

def rule_three():
    pass

def rule_four():
    pass

def rule_five():
    pass

def rule_six():
    pass

def rule_seven():
    pass

def rule_eight():
    pass

def rule_nine():
    pass

text_file = open('text.txt','r')
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
        timetable[-1].append([newpair])
        if teams[-1].get(newpair[0][0]):#teams are converted into numbers
            teams[-1][newpair[0][0]][newpair[0]]=newpair
        else:
            teams[-1][newpair[0][0]]={}
            teams[-1][newpair[0][0]][newpair[0]]=newpair
        if teams[-1].get(newpair[1][0]):#teams are converted into numbers
            teams[-1][newpair[1][0]][newpair[1]]=newpair
        else:
            teams[-1][newpair[1][0]]={}
            teams[-1][newpair[1][0]][newpair[1]]=newpair
    else:
        timetable.append([])
        teams.append({})
print(timetable)
print(teams)
        







Put in a text file called text.txt- sample data
#1
D1 C1
A1 B1
F1 E1
C2 B2
F2 A2
E2 D2
#2
D1 C1
A1 B1
F1 E1
C2 B2
F2 A2
E2 D2