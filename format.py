file_handle= open("12teambestanswer.txt", "r")

round_num=0

for lines_counter in range (183):
    temp= file_handle.readline()
    #remove /n at the end
    temp= temp[:-1]

    if temp[0]== "#":
        round_num= round_num+1

        continue
    
    player1_team= temp[0]
    finder=0
    while temp[finder]!= " ":
        finder= finder+1
    player1_number= temp[1:finder]

    
    #player1_number= temp[1]
    player2_team= temp[finder+1]
    player2_number= temp[finder+2:]
    print(str(round_num)+","+player1_team+"."+player1_number+","+player2_team+"."+player2_number)


