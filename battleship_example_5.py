from random import randint

from pip._vendor.distlib.compat import raw_input

board = []

for x in range(0, 5):
    # This will make the basic list that will eventually become the board
    board.append(["O"] * 5)


def print_board(board):
    # This will take this the existing lists within board list and print them in individual rows to make a 5 x 5 board
    for row in board:
        print(" ".join(row))


print_board(board)
print("Let's play battleship:")


# Now I'm adding code below to create a random spot to hide my/the battleship
def random_row(board):
    return randint(1, len(board))


def random_col(board):
    return randint(1, len(board[0]))


# Let's place the Battleship(s) somewhere random..
ship_row = random_row(board)
ship_col = random_col(board)
ship2_row = random_row(board)
ship2_col = random_col(board)

# Now that the battleship is hidden, I'm going to let them guess where.
print("You have Four Guesses to find either of my two Battleships. They each only occupy one space out of 25 (2 of 25 "
      "total).. Choose wisely!:")
print("For Rows & Columns, Enter A Number That's On The Board (1-5):")

for turn in range(0, 4):
    # Make a guess
    # Test that guess
    print
    # For debugging and or to cheat, you can print the ships' location before you guess if you want, but I have the statements commented out..
    # print ship_row, ship_col
    # print ship2_row, ship2_col
    print
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Column: "))

    # Now let's tell them if their guess was right or wrong..
    if (guess_row == ship_row and guess_col == ship_col) or \
            (guess_row == ship2_row and guess_col == ship2_col):
        print_board("Congratulations! You sunk my battleship!")

        print("You Win!")
        break
        # Exits the loop if they sink a battleship
    else:
        if (guess_row <= 0 or guess_row > 5) or \
                (guess_col <= 0 or guess_col > 5):
            print("Oops, that's not even in the ocean.")

        elif (board[guess_row - 1][guess_col - 1] == "X"):
            print("You guessed that one already.")

        else:
            print("You missed my battleship!")

            board[guess_row - 1][guess_col - 1] = "X"
        if turn == 3:
            print("You didn't find the Battleship(s) in time. GAME OVER!")


    print( "Turn", turn + 1)

    print_board(board)

# Let's find out where the ship was..
print("The first Battleship was in row: %s and column: %s" % (ship_row, ship_col))

print("The second Battleship was in row: %s and column: %s" % (ship2_row, ship2_col)


# print "The first Battleship was located on the board here:"
if (ship_row >= 1 and ship_col >= 1) and (ship_row <= 5 and ship_col <= 5)
    board=[ship_row - 1][ship_col - 1] = "B"
    # print_board(board)
elif ship_row == 0 and ship_col == 0:
    board=[ship_row][ship_col] = "B"
    # print_board(board)
elif ship_row == 0 and not ship_col == 0:
    board[ship_row][ship_col - 1] = "B"
    # print_board(board)
elif ship_row != 0 and ship_col == 0:
    board[ship_row - 1][ship_col] = "B"
    # print_board(board)


print("The two Battleships were located on the board here:")
if (ship2_row >= 1 and ship2_col >= 1) and (ship2_row <= 5 and ship2_col <= 5):
    board[ship2_row - 1][ship2_col - 1] = "B"
    print_board(board)
elif ship2_row == 0 and ship2_col == 0:
    board[ship2_row][ship2_col] = "B"
    print_board(board)
elif ship2_row == 0 and not ship2_col == 0:
    board[ship2_row][ship2_col - 1] = "B"
    print_board(board)
elif ship2_row != 0 and ship2_col == 0:
    board[ship2_row - 1][ship2_col] = "B"
    print_board(board)
