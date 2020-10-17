###################################
#########   Battleship  ###########
###################################
from random import randint

###################################
EASY = "EASY"
HARD = "HARD"
No = "No"
Yes = "Yes"
game_still_going = True
EMPTY = "0"
player1 = "X"
player2 = "Y"
size = "6"
Lv = EASY
name = "player"
name2 = "player2"
multi = "1" 
live = "10"
win = "GAME OVER"
game = 3
ship = No
row = 1
col = 1
row2 = 1
col2 = 1
option_board = [ str(name), int(size), str(Lv), str(multi), str(name2), int(live), str(win), int(game), str(ship), int(row), int(col), int(row2), int(col2)]
##################################

def menu_main():
    clean()
    print("----------------------------\n")
    print("--------Battleship----------\n")
    print("       CHOOSE OPTION        \n\n")
    print("GAME----------------PRESS---1")
    print("OPTION--------------PRESS---2")
    print("EXIT GAME-----------PRESS---3\n")
    input1= input("CHOOSE :   ")
    try:
        main_choose = int(input1)
        return main_choose
    except ValueError:
        return

def menu_game():    
    clean()
    print("----------------------------\n")
    print("--------Battleship----------\n")
    print("       CHOOSE GAME        \n")
    print("ONE PLAYER ------ PRESS --- 1 ")
    print("TWO PLAYER------- PRESS --- 2 ")
    print("PLAYER VS AI----- PRESS --- 3 ")
    print("BACK------------- PRESS --- 4 \n")
    input2 = input("CHOOSE GAME :   ")
    clean()
    try:
        option_board[7] = int(input2)
        return option_board[7]
    except ValueError: 
        input("\n\n WRONG CHOOSE")
        return

def menu_option(option_board):
    back = 1 
    while back:
        clean()
        print("\n  ")
        print("PLAYER - 1 NAME:            ", option_board[0], "          IF YOU WANT CHANGE PRESS N \n")
        print("PLAYER - 2 NAME:            ", option_board[4], "         IF YOU WANT CHANGE PRESS P \n")
        print("SIZE OF ARRAY:                ", option_board[1], "             IF YOU WANT CHANGE PRESS A \n")
        print("AI LEVEL:                    ", option_board[2], "           IF YOU WANT CHANGE PRESS L \n")
        print("NUMBER OF BOARD:              ", option_board[3], "             IF YOU WANT CHANGE PRESS M \n")
        print("NUMBER OF TURN:               ", option_board[5], "            IF YOU WANT CHANGE PRESS T \n") 
        print("INPUT SHIP:                   ", option_board[8], "            IF YOU WANT CHANGE PRESS I \n")     
        print("BACK                                          IF YOU WANT BACK PRESS B \n")
        input3 = input("CHOOSE OPTION :   ")
        if input3 == "N" or input3 == "n":      
            option_board[0] = change_name(name)           
        elif input3 == "A" or input3 == "a":
            option_board[1] = change_size(size)        
        elif input3 == "L" or input3 == "l":
            option_board[2] = change_lv(Lv)      
        elif input3 == "M" or input3 == "m":
            option_board[3] = number_board(multi) 
        if input3 == "P" or input3 == "p":      
            option_board[4] = change_name(name2)
        elif input3 == "T" or input3 == "t":
            option_board[5] = change_live(option_board[5])
        elif input3 == "I" or input3 == "i":
            option_board[8] = in_ship(ship) 
            if option_board[8] == "Yes":
                option_board[9] = input_ship_x()
                option_board[10] = input_ship_y()
                option_board[11] = input_ship_x()
                option_board[12] = input_ship_y()
                print(option_board)
                input("Press Enter")
                return row, col
            else:
                pass

        elif input3 == "B" or input3 == "b":
             back = 0
        else:
            pass   
    return option_board

def change_name(name):
    name = input("ENTER YOUR NEW NAME:  ") 
    return name

def change_size(size):
    input4 = input("CHOOSE SIZE OF ARRAY: ")
    try:
        size = int(input4)
        return size
    except ValueError:
        return size

def change_lv(Lv):
    if option_board[2] == "EASY":
        return "HARD"
    elif option_board[2] == "HARD":
        return "EASY"

def number_board(multi):
    if option_board[3] == "1":
        return "2"
    elif option_board[3] == "2":
        return "1"

def change_live(live):
    input5 = input("HOW MANY LIVS YOU WANT: ")
    try:
        option_board[5] = int(input5)
        return option_board[5]
    except ValueError:
        return option_board[5]
    
def in_ship(ship):
    if option_board[8] == "No":
        return "Yes"
    elif option_board[8] == "Yes":
        return "No"

def input_ship_x():
    while True:
        try:
            x = int(input("Input ship row: "))
            in_ship_row = int(x)-1
            return in_ship_row
        except ValueError:
            print("Try again: ")
        else:
            return in_ship_row

def input_ship_y():
    while True:
        try:
            y = int(input("Input ship col: "))
            in_ship_col = int(y)
            return in_ship_col-1
        except ValueError:
            print("Try again: ")
        else:
            return in_ship_col


def one_player(board, game_still_going, board2, option_board): 
    turn = 1
    player = "X"
    player = init_move1(board, game_still_going, board2, option_board, turn, player)
    return player

def two_player(board, game_still_going, board2, option_board):     
    player = "Y"
    turn = 1
    player = init_move1(board, game_still_going, board2, option_board, turn, player)
    return player    

def ai_vs_player(board, game_still_going, board2, option_board):
    player = "Y"
    turn = 1
    player = init_move1(board, game_still_going, board2, option_board, turn, player)
    return player   

def ai_hard_vs_player(board, game_still_going, board2, option_board):
    player = "Y"
    turn = 1
    player = init_move1(board, game_still_going, board2, option_board, turn, player)
    return player

def ship_choose(board, board2, option_board):

    if option_board[8] == "Yes" and option_board[9] >= 0 and option_board[9] <= option_board[1] and option_board[10] >= 0 and option_board[10] <= option_board[1]and option_board[11] >= 0 and option_board[11] <= option_board[1] and option_board[12] >= 0 and option_board[12] <= option_board[1]: 
        choose_size(board, board2, option_board)
        print_board(board, board2, option_board)
        ship_row = option_board[9]
        ship_col = option_board[10]
        ship2_row = option_board[11]
        ship2_col = option_board[12]
        

    else:
        if option_board[3] == "1":
            choose_size(board, board2, option_board)
            print_board(board, board2, option_board)
            ship_row, ship_col = random_ship(board)
            ship2_row = option_board[11]
            ship2_col = option_board[12]
            print(ship_row+1, ship_col+1)
        
            
            
        elif option_board[3] == "2":
            choose_size(board, board2, option_board)
            print_board(board, board2, option_board)
            ship_row, ship_col = random_ship(board)
            ship2_row, ship2_col = random_ship2(board2)
            print(ship_row+1, ship_col+1)
            print(ship2_row+1, ship2_col+1)

    return ship_row, ship_col, ship2_row, ship2_col
       

def init_move1(board, game_still_going, board2, option_board, turn, player):

    ship_row, ship_col, ship2_row, ship2_col = ship_choose(board, board2, option_board)
   
    
    while game_still_going:        
        if turn <=option_board[5]:
            if option_board[7] == 2 or  option_board[7] == 3 or option_board[3] == "2" :
                player = flip_player(player)        

            if player == "X":
                guess_row, turn= shotx(board, board2, option_board, player, turn)
                guess_col, turn = shoty(board, board2, option_board, player, turn)
                if guess_row == ship_row and guess_col == ship_col:
                    print("Congratulations! You hit ship!")
                    board[ship_row][ship_col] = "+"
                    game_still_going = False
                    option_board[6] = "Winner is:  "
                elif (guess_row < 0 or guess_row > int(option_board[1]-1)) or (guess_col < 0 or guess_col > int(option_board[1]-1)):
                    print("Aim at the sea")
                    input("Press Enter...")
                elif (board[guess_row][guess_col]) == "X" or (board[guess_row][guess_col]) == "Y":
                    print("Try again or surrender!")
                    input("Press Enter...")
                else:
                    print("You missed!")
                    board[guess_row][guess_col] = player
                turn = turn + 1

            elif player == "Y" and  option_board[3] == "1" and option_board[7] != 3 :
                guess_row, turn= shotx(board, board2, option_board, player, turn)
                guess_col, turn = shoty(board, board2, option_board, player, turn)
                if guess_row == ship_row and guess_col == ship_col:
                    print("Congratulations! You hit ship!")
                    board[ship_row][ship_col] = "#"
                    game_still_going = False
                    option_board[6] = "Winner is:  "
                elif (guess_row < 0 or guess_row > int(option_board[1]-1)) or (guess_col < 0 or guess_col > int(option_board[1]-1)):
                    print("Aim at the sea")
                    input("Press Enter...")
                elif(board[guess_row][guess_col]) == "X" or (board[guess_row][guess_col]) == "Y":
                    print("Try again or surrender!")
                    input("Press Enter...")
                else:
                    print("You missed!")
                    board[guess_row][guess_col] = player
                turn = turn + 1

            elif player == "Y" and  option_board[3] == "2" and option_board[7] != 3 :
                guess_row, turn= shotx(board, board2, option_board, player, turn)
                guess_col, turn = shoty(board, board2, option_board, player, turn)
                if guess_row == ship2_row and guess_col == ship2_col:
                    print("Congratulations! You hit ship!")
                    board2[ship2_row][ship2_col] = "#"
                    game_still_going = False
                    option_board[6] = "Winner is:  "
                elif (guess_row < 0 or guess_row > int(option_board[1]-1)) or (guess_col < 0 or guess_col > int(option_board[1]-1)):
                    print("Aim at the sea")
                    input("Press Enter...")
                elif(board2[guess_row][guess_col]) == "X" or (board2[guess_row][guess_col]) == "Y":
                    print("Try again or surrender!")
                    input("Press Enter...")
                else:
                    print("You missed!")
                    board2[guess_row][guess_col] = player
                turn = turn + 1

            elif player == "Y" and  option_board[3] == "2" and option_board[7] == 3:
                guess_row, guess_col, turn= shot_comp(board, board2, option_board, player, turn)
                if guess_row == ship2_row and guess_col == ship2_col:
                    print("Congratulations! You hit ship!")
                    board2[ship2_row][ship2_col] = "#"
                    game_still_going = False
                    option_board[6] = "Winner is:  "
                elif (guess_row < 0 or guess_row > int(option_board[1]-1)) or (guess_col < 0 or guess_col > int(option_board[1]-1)):
                    print("Aim at the sea")
                    input("Press Enter...")
                elif(board2[guess_row][guess_col]) == "X" or (board2[guess_row][guess_col]) == "Y":
                    print("Try again or surrender!")
                    input("Press Enter...")
                else:
                    print("You missed!")
                    board2[guess_row][guess_col] = player
                turn = turn + 1

            elif player == "Y" and  option_board[3] == "2" and option_board[7] == 3 and option_board[2] != EASY:
                guess_row, guess_col, turn= shot_comp(board, board2, option_board, player, turn)
                if guess_row == ship2_row or guess_col == ship2_col:
                    print("Congratulations! You hit ship!")
                    board2[ship2_row][ship2_col] = "#"
                    game_still_going = False
                    option_board[6] = "Winner is:  "
                elif (guess_row < 0 or guess_row > int(option_board[1]-1)) or (guess_col < 0 or guess_col > int(option_board[1]-1)):
                    print("Aim at the sea")
                    input("Press Enter...")
                elif(board2[guess_row][guess_col]) == "X" or (board2[guess_row][guess_col]) == "Y":
                    print("Try again or surrender!")
                    input("Press Enter...")
                else:
                    print("You missed!")
                    board2[guess_row][guess_col] = player
                turn = turn + 1

            elif player == "Y" and  option_board[3] == "1" and option_board[7] == 3 :
                guess_row, guess_col, turn= shot_comp(board, board2, option_board, player, turn)
                if guess_row == ship_row and guess_col == ship_col:
                    print("Congratulations! You hit ship!")
                    board[ship_row][ship_col] = "#"
                    game_still_going = False
                    option_board[6] = "Winner is:  "
                elif (guess_row < 0 or guess_row > int(option_board[1]-1)) or (guess_col < 0 or guess_col > int(option_board[1]-1)):
                    print("Aim at the sea")
                    input("Press Enter...")
                elif(board[guess_row][guess_col]) == "X" or (board[guess_row][guess_col]) == "Y":
                    print("Try again or surrender!")
                    input("Press Enter...")
                else:
                    print("You missed!")
                    board[guess_row][guess_col] = player
                turn = turn + 1

            elif player == "Y" and  option_board[3] == "1" and option_board[7] == 3 and option_board[2] != EASY:
                guess_row, guess_col, turn= shot_comp(board, board2, option_board, player, turn)
                if guess_row == ship_row or guess_col == ship_col:
                    print("Congratulations! You hit ship!")
                    board[ship_row][ship_col] = "#"
                    game_still_going = False
                    option_board[6] = "Winner is:  "
                elif (guess_row < 0 or guess_row > int(option_board[1]-1)) or (guess_col < 0 or guess_col > int(option_board[1]-1)):
                    print("Aim at the sea")
                    input("Press Enter...")
                elif(board[guess_row][guess_col]) == "X" or (board[guess_row][guess_col]) == "Y":
                    print("Try again or surrender!")
                    input("Press Enter...")
                else:
                    print("You missed!")
                    board[guess_row][guess_col] = player
                turn = turn + 1

        else:    
            game_still_going = False
            end_game()   
        print_board(board, board2, option_board)
    return player
                  

def who_win(winner):
    print("\n", option_board[6], winner)
    option_board[6] = " GAME OVER "
    input("\nPress Enter...")
    return 

def flip_player(player):
    if player == "X":
        return "Y"
    elif player == "Y":
        return "X"

def random_ship(board):
    ship_row = randint(0, len(board) - 1)
    ship_col = randint(0, len(board[0]) - 1)
    return ship_row, ship_col

def random_ship2(board2):
    ship2_row = randint(0, len(board2) - 1)
    ship2_col = randint(0, len(board2[0]) - 1)
    return ship2_row, ship2_col

def choose_size(board, board2, option_board):
    if option_board[3] == "1":
        for col in range(int(option_board[1])):
            board.append(["O"] * (int(option_board[1])))
    elif option_board[3] == "2":
        for col in range(int(option_board[1])):
            board.append(["O"] * (int(option_board[1])))
        for X in range(int(option_board[1])):
            board2.append(["O"] * (int(option_board[1])))  
        print(col, X)

def print_board(board, board2, option_board):  
    if option_board[3] == "1":
        print("\n")
        print(option_board[0])
        print("\n") 
        for row in board:
            print("----"*int(size))
            print((" | ").join(row) )
        return board  
    elif option_board[3] == "2":
        print("\n")
        print(option_board[0])
        print("\n")
        for row in board:
            print("----"*int(size))
            print((" | ").join(row) )
        print("\n")
        print("===="*int(size))
        print("\n")
        print(option_board[4])
        print("\n")
        for row in board2:
            print("----"*int(size))
            print((" | ").join(row) )
    return board, board2

def shotx(board, board2, option_board, player, turn):
    print("\nNow is turn:", player)   
    print("\nTurn number: ", turn, "\n")
    
    while True:
        try:
            x = input("Guess Row: ")
            if x == "salva":
                print("\n\n    Wielka przewaga gracza: ", player, " o imieniu:  ", option_board[0], "\n\n      Wielkie gratulacje dla niego!!!!")
                print("\nWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW+........-#WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW+.-..........-WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW*.#............*WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW+*-.-:....:-...+WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW=+.#WW@..WWW#::=WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW*.*@*.*:.=@+-#WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW*....-@=.....*WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@##......*@WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWWWWW:..+WWWWW@.*=**+*@:-WWWWWWW+:=WWWWWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWW@.......#WWWW:.==*#*=.+WWWWW*....-#WWWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWW=...*+:...:#WW=......#WWW#:....-...+WWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWWWWWWW#*-......+@WWWWW=:.....-..-:+=WWWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@*-....-*:....-*@WWWWWWWWWWWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@+:+-....+@WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWWW*::+++:-......:=W@+.....+=@WWWWWWWWWWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWW*.........-*@WWWWWWWWW#+.-:.....:.*WWWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWWWW#.:*--#WWWWWWWWWWWWWWWWW*.+--.-+@WWWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@++@WWWWWWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW")
                input("\n\n Press enter")
                end_game()
                main(option_board)
            elif x == "b":
                end_game()
                main(option_board)
                
            guess_row = int(x) - 1
            return guess_row, turn
        except ValueError:
            print("Try again: ")
        else:
            return guess_row, turn


def shoty(board, board2, option_board, player, turn):
   
    while True:
        try:
            y = int(input("Guess Col: "))
            if y == "b":
                end_game()
                main(option_board)
            guess_col = int(y) - 1
            clean()
            return guess_col, turn
        except ValueError:
            print("Try again: ")
        else:
            return guess_col, turn

def shot_comp(board, board2, option_board, player, turn):
    print("\nNow is turn computer:", player)   
    print("\nTurn number: ", turn, "\n")
    x = randint(0, len(board) - 1)
    y = randint(0, len(board[0]) - 1)
    print(x+1, y+1)
    input("Press Enter")
    clean()
    guess_row = x
    guess_col = y 
    return guess_row, guess_col, turn


def clean():
    import os
    os.system("cls || clear")

def end_game():
    print("\n\n-----------    END GAME    ------------")
    print("\n")
    x = input("\nPlay again? (y/n)  ")
    clean()
    if x == "y":
        pass
        return 
    else:
        input("\nPress Enter")
        ex = 1
        return ex

def return_game():
    pass

def main(option_board):
    clean()
    ex = 1
    while ex:      
        board = []
        board2 = []       
        choose_menu = menu_main()
        while choose_menu is None:
            choose_menu = menu_main()
        if choose_menu == 1:
            start = menu_game()
            while start is None:
                 start = menu_main()
            if start == 1:
                winner = one_player(board, game_still_going, board2, option_board)
                who_win(winner)
                del board 
                del board2
            elif start == 2:
                winner = two_player(board, game_still_going, board2, option_board)
                who_win(winner)
                del board
                del board2
            elif start == 3:
                Lv = EASY
                if Lv == EASY:
                    winner = ai_vs_player(board, game_still_going, board2, option_board)
                    who_win(winner)
                    del board
                    del board2
                else:
                    winner = ai_hard_vs_player(board, game_still_going, board2, option_board)
                    who_win(winner)
                    del board
                    del board2
            elif start == 4:
                return_game()
            else:
                input("Choose number...")
        elif choose_menu == 2:
            menu_option(option_board)
        elif choose_menu == 3:
            print("\n\n-----------    END GAME    ------------")
            input("\nPress Enter")
            ex = 0

main(option_board)