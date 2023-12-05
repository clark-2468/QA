

current_num=[]

#generator
#make 6 digits number using 1,1,2,2,3,3
valid_counter=0

for trying_every_num in range(111111,332299):
    current_num=str(trying_every_num)
    #print(current_num)
    valid=True
    valid1=True

    #made of 1 1 2  2 3 3
    for counting in range (6):
        checking=int(current_num[counting])
        if checking >3:
            valid1=False
            valid=False
            break
        if checking==0:
            valid1=False
            valid=False
            break
    
    #no numbers appear more than twice
    if valid1==True:

        for counting in range (6):
            checking=int(current_num[counting])
            if current_num.count(str(checking))>2:
                valid1=False
                valid=False
                break
    #no consecutive pairs of numbers
            
    if valid1==True:
        first_pair=current_num[0:2]
        second_pair=current_num[2:4]
        third_pair=current_num[4:6]
        fourth_pair=current_num[1:3]
        fifth_pair=current_num[3:5]
        if first_pair==second_pair:
            valid=False
        elif second_pair==third_pair:
            valid=False
        elif fifth_pair==fourth_pair:
            valid=False
        

    if valid==True:
        valid_counter+=1
        print(current_num)






print(valid_counter)

#no working