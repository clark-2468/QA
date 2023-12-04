



def flooring(input_number):
    #the largest integer less than or equal to x

    return int(input_number)

def ceiling(input_number):
    #the smallest integer greater than or equal to x

    return int(input_number)+1


def F(a):
    re=a
    re=flooring(a)
    re=re+a**2
    re=ceiling(re)
    re=re+a**3
    re=flooring(re)
    re=re+a**4
    re=ceiling(re)

    print(re)

#a=float(input("Enter the number: "))
#F(a)

for i in range(100,300,1):
    i=float(i)
    i=i/100
    print(i)
    F(i)