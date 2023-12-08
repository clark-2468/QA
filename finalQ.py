#code for rules first

def rule2(player1, player2):
    #players do not play against its team mate
    if player1[0]==player2[0]:
        return False
    