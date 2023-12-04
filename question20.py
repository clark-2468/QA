

current_num=[]

#generator
#make 6 digits number using 1,1,2,2,3,3
def make_num():
    for i in range(1,4):
        for j in range(1,4):
            for k in range(1,4):
                if i!=j and j!=k and k!=i:
                    current_num.append(i*100+j*10+k)
    return current_num

current_num=make_num()
print(current_num)