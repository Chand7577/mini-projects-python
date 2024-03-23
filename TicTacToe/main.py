from TicTacToe.module import create_board,check_turn,win_check
import os 
map={1:'1',2:'2',3:'3',
     4:'4',5:'5',6:'6',
     7:'7',8:'8',9:'9'
     }


playing=True
turn=0
complete=False
while playing:
    for dots in range(0,10):
        print('.',end="")
    print('Welcome to the Tic Tac Toe game',end="")
    for dots in range(0,10):
        print('.',end='')
    print()
    create_board(map)
    print(f'player {(turn%2)+1} turn')

    userVal=input('Choose a number from the above given matrix or q to quite the game').strip()
    
    if userVal=='q':
        playing=False
    
    elif userVal.isdigit() and int(userVal) in range(1,10):
         if(map[int(userVal)] not in {'X','O'}):
            turn+=1
            map[int(userVal)]=check_turn(turn)
            create_board(map)
            os.system('cls' if os.name="nt"  else "cls" )
            if(win_check(map)):
                complete=True
                playing=False
            if(turn>8):
               print('Draw match')

if(complete):
    create_board(map)
    if(check_turn(turn)=='X'):
        print('X has won the game')

    else:
        print('Y has won')





print('Thanks for playing')
        
    
    
    
