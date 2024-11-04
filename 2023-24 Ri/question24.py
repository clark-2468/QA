def base(number,base):
    number = str(number)
    re1=int(number[0])*base 
    re2=int(number[1])
    re=re1+re2
    #print(re)
    return re

#base(46,58)
#base(58,46)


for i1 in range(10,100):
    for i2 in range(10,100):
        if base(i1,i2)==base(i2,i1):
            print(i1,i2)


#working