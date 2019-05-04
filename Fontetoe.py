# Tic Tac Toe using Loops, funcitons, lists, and the min-max algorithm

import os
import time
import random

# Defining the board
# Tic-tac-toe 3x3
dimension = 3
my_board = [[[" " for col in range(dimension)] for col in range(dimension)] for row in range(dimension)]



def win2D(my_board):
    return False

def win3D(my_board):
    if ( (my_board[0][0][0] == my_board[1][0][0] == my_board[2][0][0])  # 3D Tower 0
    or (my_board[0][1][0] == my_board[1][1][0] == my_board[2][1][0] ) # 3D Tower 1
    or (my_board[0][2][0] == my_board[1][2][0] == my_board[2][2][0])  # 3D Tower 2
    or (my_board[0][0][1] == my_board[1][0][1] == my_board[2][0][1])  # 3D Tower 3
    or (my_board[0][1][1] == my_board[1][1][1] == my_board[2][1][1])  # 3D Tower 4
    or (my_board[0][2][1] == my_board[1][2][1] == my_board[2][2][1])  # 3D Tower 5
    or (my_board[0][0][2] == my_board[1][0][2] == my_board[2][0][2])  # 3D Tower 6
    or (my_board[0][1][2] == my_board[1][1][2] == my_board[2][1][2])  # 3D Tower 7
    or (my_board[0][2][2] == my_board[1][2][2] == my_board[2][2][2])  # 3D Tower 8
    or (my_board[0][0][0] == my_board[1][0][1] == my_board[2][0][2])  # 3D Vertical Diagonal
    or (my_board[2][0][0] == my_board[1][0][1] == my_board[0][0][2]) # 3D Vertical Diagonal
    or (my_board[0][1][0] == my_board[1][1][1] == my_board[2][1][2])  # 3D Vertical Diagonal
    or (my_board[2][1][0] == my_board[1][1][1] == my_board[0][1][2])  # 3D Vertical Diagonal
    or (my_board[0][2][0] == my_board[1][2][1] == my_board[2][2][2])  # 3D Vertical Diagonal
    or (my_board[2][2][0] == my_board[1][2][1] == my_board[0][2][2])  # 3D Vertical Diagonal
    or (my_board[0][0][0] == my_board[1][1][0] == my_board[2][2][0])  # 3D Horizontal Diagonal
    or (my_board[2][0][0] == my_board[1][1][0] == my_board[0][2][0]) # 3D Horizontal Diagonal
    or (my_board[0][0][1] == my_board[1][1][1] == my_board[2][2][1])  # 3D Horizontal Diagonal
    or (my_board[2][0][1] == my_board[1][1][1] == my_board[0][2][1])  # 3D Horizontal Diagonal
    or (my_board[0][0][2] == my_board[1][1][2] == my_board[2][2][2])  # 3D Horizontal Diagonal
    or (my_board[2][0][2] == my_board[1][1][2] == my_board[0][2][2])  # 3D Horizontal Diagonal
    or (my_board[0][0][0] == my_board[1][1][1] == my_board[2][2][2])  # 3D Cross Diagonal
    or (my_board[2][0][0] == my_board[1][1][1] == my_board[0][2][2])  # 3D Cross Diagonal
    or (my_board[0][0][2] == my_board[1][1][1] == my_board[2][2][0])  # 3D Cross Diagonal
    or (my_board[0][2][0] == my_board[1][1][1] == my_board[2][0][2]) ):  # 3D Cross Diagonal
        return True
    return False

def printHeader():
    print("""Welcome to Tic Tac Toe!""")

def playerOne():
    print('Please enter position you want to put X: ')
    pos = input('Please enter position you want to put X: ')

def insertX(layer, pos):


def playerTwo():
    print('Please enter position you want to put O: ')
    pos = input('Please enter position you want to put X: ')
    if isEmptyLayerOne(pos):
        
    elif isEmptyLayerTwo(pos):

    elif isEmptyLayerThree(pos):

    return ('Sorry, all full')
def insertO(layer, pos):

def spaceIsFree(pos):
    return my_board[pos] == ' '


def printBoard(my_board):
    count = 0
    for i in my_board:
        count += 1
        print('Layer ' + str(count))
        for j in i:
            print('')
            for k in j:
                print(k + '|', end='')
                print('_', end='')
        print('')

def compMove():
    pass


def selectRandom(my_board):
    pass


def isEmptyLayerOne(pos):
    #pos is from 0 - 8 but user chooses from 1 - 9
    row = pos//3
    col = pos%3
    if(my_board[0][row][col] == ' '):
        return True
    return False


def isEmptyLayerTwo(pos):
    #pos is from 0 - 8 but user chooses from 1 - 9
    row = pos//3
    col = pos%3
    if(my_board[1][row][col] == ' '):
        return True
    return False


def isEmptyLayerThree(pos):
    #pos is from 0 - 8 but user chooses from 1 - 9
    row = pos//3
    col = pos%3
    if(my_board[2][row][col] == ' '):
        return True
    return False



def isFull(my_board):
    if my_board.count(' ') > 1:  # Since we always have one blank element in board we must use > 1
        return False
    return True


def main():
    printHeader()


if __name__ == "__main__":
    printBoard(my_board)


