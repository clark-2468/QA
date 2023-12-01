import math

x=12**3
y=45**6
n=78**9
sqrt5=math.sqrt(5)
r=1+sqrt5
r=r/2

seq=[0]
seq.append(x)
seq.append(y)
print(seq)
def nextu(n):
    global seq,r

    
    if n==0:
        pre_loc=2
        pre_2_loc=1
    elif n==1:
        pre_loc=0
        pre_2_loc=2
    elif n==2:
        pre_loc=1
        pre_2_loc=0
    #print(pre_loc,pre_2_loc)
    next=r*seq[pre_loc]-seq[pre_2_loc]
    
    #print("term",n+1,"is")
    #print(next)
    return next
#u=3
for i in range (3,n+1,3):
    #3 4 5
    #6 7 8
    #print(seq)
    for i2 in range(3):
        
        re=nextu(i2)
        seq[i2]=re
        #u=u+1

#0=u3
#1=u4
#2=u5


print(seq)
