sum=0
for trail in range (1000000000,10000000000):
    #digits can repeat
    valid=True
    for digit in range(10):
        if str(trail).count(str(digit)) !=1:
            valid=False
            break
    if valid:
            #print(str(trail))
                #break the trail into digits of two
            frag=[]
            for fragments in range(5):
                fragtoappend=str(trail)[fragments*2:fragments*2+2]
                #print(fragtoappend)
                frag.append(fragtoappend)
                #print(frag)
            #check if the fragments are in an alritmetic sequence
            if int(frag[1])-int(frag[0])==int(frag[2])-int(frag[1])==int(frag[3])-int(frag[2])==int(frag[4])-int(frag[3]):
                #print(trail)
                #add all fragments up
                sum+=int(frag[0])+int(frag[1])+int(frag[2])+int(frag[3])+int(frag[4])
                print(sum)
print(sum)

#with 0 in front

sum22=0
for trail in range (100000000,1000000000):
    #digits can repeat
    valid=True
    trailstr=str(trail)
    trailstr="0"+trailstr
    for digit in range(10):
        if trailstr.count(str(digit)) !=1:
            valid=False
            break
    if valid:
            #print(str(trail))
                #break the trail into digits of two
            frag=[]
            for fragments in range(5):
                fragtoappend=trailstr[fragments*2:fragments*2+2]
                #print(fragtoappend)
                frag.append(fragtoappend)
                #print(frag)
            #check if the fragments are in an alritmetic sequence
            if int(frag[1])-int(frag[0])==int(frag[2])-int(frag[1])==int(frag[3])-int(frag[2])==int(frag[4])-int(frag[3]):
                #print(trail)
                #add all fragments up
                sum22+=int(frag[0])+int(frag[1])+int(frag[2])+int(frag[3])+int(frag[4])
                print(sum22)
print(sum22)


                               
