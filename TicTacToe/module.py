def create_board(map):
    board=(f"|{map[1]}|{map[2]}|{map[3]}|\n|{map[4]}|{map[5]}|{map[6]}|\n|{map[7]}|{map[8]}|{map[9]}|")

    print(board)


def check_turn(turn):
    if (turn%2==0) :return 'O'
    else: return 'X'


def win_check(map):
    #horizontal check
    if map[1]==map[2]==map[3] or map[4]==map[5]==map[6] or map[7]==map[8]==map[9]:
        return True
    #vertical check

    elif(map[1]==map[4]==map[7] or map[2]==map[5]==map[8] or map[3]==map[6]==map[9]):
        return True
    #diagonal check
    elif(map[1]==map[5]==map[9] or map[3]==map[5]==map[7]):
        return True
    else:
        return False






