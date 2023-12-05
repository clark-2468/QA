#fibonacci sequence
from decimal import *
getcontext().prec = 100

import math

def calA(side_a, side_b,side_c):
    
    semi_perimeter = (side_a + side_b + side_c)/2
    area = semi_perimeter*(semi_perimeter-side_a)*(semi_perimeter-side_b)*(semi_perimeter-side_c)
    area = Decimal(math.sqrt(area))
    return area

def fibonaaci():
    fib = [0,1]
    while True:
        if fib[-1] + fib[-2] < 99999999999999999999999999999:
            fib.append(fib[-1] + fib[-2])
        else:
            break
    return fib

seq=fibonaaci()
print(seq)

for n in range(1,len(seq)):
    a=Decimal(seq[n+2])
    
    b=Decimal(seq[2*n+1])
    b=math.sqrt(Decimal(b))
    b=Decimal(b)
    c1=Decimal(seq[n+1])
    c2=Decimal(seq[2*n+2])
    c2=math.sqrt(Decimal(c2))
    c=c1+Decimal(c2)
    c=Decimal(c)
    #print(a,b,c)
    area=calA(a,b,c)
    print(area)
    if int(area)==area and area>0:
        print("got it")
        print(area)
        
