import numpy as np
import Battleship as bs
 
 
class Board:
    def __init__(self):
        self.grid = np.array([['.' for i in range(10)] for j in range(10)])
 
    def __str__(self):
        return "Gameboard"
 
    def show_board(self):
        for i in range(10):
            print(" {} ".format(chr(i+65)), end="")
        print(' /')
        for i in range(10):
            for j in range(10):
                print("[{}]".format(self.grid[i][j]), sep="", end="")
            print('', i + 1, end="")
            print()
        print()
 
    def check_field(self, x, y):
        if x is not str:
            return False;
        return self.grid[ord(x.upper())-65][int(y)]
 
    def put_ship(self, x: bs, field: str, direction: str = "E"):
        alert = "";
        if field[0].upper() not in "ABCDEFGHIJ":
            alert += "\nInvalid column letter. Enter letter from \"A\" to \"J\"."
 
        if not 0 < int(field[1]) < 11:
            alert += "\nInvalid row number. Enter number from \"1\" to \"10\"."
 
        if not alert and self.check_field(field[0], field[1]) != ".":
            alert += "\nField {} is not empty.".format(field)
 
        if direction not in ("N", "E", "S", "W"):
            alert += "\nWrong direction. Enter one of: {}.".format(("N", "E", "S", "W"))
 
        if alert is "":
            return True
 
        else:
            print(alert)
            return False
