#-------GLOBAL VARIABLES---------#
Console= ["_","_","_",
          "_","_","_",
          "_","_","_",]
game_not_end= True
player_turn = "X"
turn=0

# Displaying the game board
def display_console():
    global Console
    print("-","-","-","-","-")
    print("|",Console[0],Console[1],Console[2],"|")
    print("|",Console[3],Console[4],Console[5],"|")
    print("|",Console[6],Console[7],Console[8],"|")
    print("-","-","-","-","-")

# Checking win condition in rows
def check_row(player):
    player=str(player)
    global game_not_end
    #Row 1
    if Console[0]==Console[1]==Console[2]!="_":
        print("Player "+player+ " WINS!!")
        Console[0]=Console[1]=Console[2]="-"
        display_console()
        print("GAME OVER")
        game_not_end=False
    #Row 2
    elif Console[3]==Console[4]==Console[5]!="_":
        print("Player "+player+ " WINS!!")
        Console[3]=Console[4]=Console[5]="-"
        display_console()
        print("GAME OVER")
        game_not_end=False
    #Row 3
    elif Console[6]==Console[7]==Console[8]!="_":
        print("Player "+player+ " WINS!!")
        Console[6]=Console[7]=Console[8]="-"
        display_console()
        print("GAME OVER")
        game_not_end=False
    else:
        game_not_end = True

# Checking win condition in coloumns
def check_col(player):
    player=str(player)
    global game_not_end
    #Column 1
    if Console[0]==Console[3]==Console[6]!="_":
        print("Player "+player+ " WINS!!")
        Console[0]=Console[3]=Console[6]="|"
        display_console()
        print("GAME OVER")
        game_not_end=False
    #Column 2
    elif Console[1]==Console[4]==Console[7]!="_":
        print("Player "+player+ " WINS!!")
        Console[1]=Console[4]=Console[7]="|"
        display_console()
        print("GAME OVER")
        game_not_end=False
    #Column 3
    elif Console[2]==Console[5]==Console[8]!="_":
        print("Player "+player+ " WINS!!")
        Console[2]=Console[5]=Console[8]="|"
        display_console()
        print("GAME OVER")
        game_not_end=False
    else:
        game_not_end=True

# Checking win condition in diagonals
def check_diag(player):
    player=str(player)
    global game_not_end
    #diagonal 1
    if Console[0]==Console[4]==Console[8]!="_":
        print("Player "+player+ " WINS!!")
        Console[0]=Console[4]=Console[8]="\\"
        display_console()
        print("GAME OVER")
        game_not_end=False
    #diagonal 2
    elif Console[6]==Console[4]==Console[2]!="_":
        print("Player "+player+ " WINS!!")
        Console[6]=Console[4]=Console[2]="/"
        display_console()
        print("GAME OVER")
        game_not_end=False
    else:
        game_not_end=True

#Checking win condition
def check_win(player):
    player= str(player)
    if game_not_end== True:
        check_row(player)
    if game_not_end== True:
        check_col(player)
    if game_not_end== True:
        check_diag(player)

#Playing Tic-Tac-Toe
def play(player):
    global Console
    global turn
    global game_not_end
    player= str(player)
    invalid_pos= True
    #checking correct entry
    while invalid_pos:
        pos= input("Please select a position between 1 to 9  ")
        if (pos=="1" or pos=="2" or pos=="3" or pos=="4" or pos=="5" or pos=="6" or pos=="7" or pos=="8" or pos=="9"):
            if(Console[int(pos)-1]== "_"):
                invalid_pos=False
            else:
                print("Place already taken!")
        else:
            print("Invalid Position!")
    #printing result
    pos= int(pos)
    pos=pos-1
    Console[pos]=player
    turn=turn+1
    display_console()
    if game_not_end== True:
        check_win(player)
    if(game_not_end== True):
        if(turn==9):
            print("GAME TIED!!")
            game_not_end = False

#Switching player for the next turn            
def switch_player():
    global player_turn
    if player_turn =="X":
        player_turn = "O"
    elif player_turn == "O":
        player_turn = "X"

#Lets Play        
while True:
    print("GAME IS ON!!")
    display_console()
    while game_not_end:
        print("Player "+ player_turn+ "'s turn")
        if game_not_end== True:
            play(player_turn)
        if game_not_end== True:
            switch_player()
    y_n= input("Do you want to play again? y or n ")
    y_n.lower()
    if y_n== 'n':
        break
    if y_n == 'y':
        print("LETS PLAY AGAIN!!")
        game_not_end = True
        Console= ["_","_","_",
          "_","_","_",
          "_","_","_",]
        player_turn = "X"
        turn=0


