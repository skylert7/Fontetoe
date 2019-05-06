#   __          __  _                            _          ______          _       _             _
#   \ \        / / | |                          | |        |  ____|        | |     | |           | |
#    \ \  /\  / /__| | ___ ___  _ __ ___   ___  | |_ ___   | |__ ___  _ __ | |_ ___| |_ ___   ___| |
#     \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \  |  __/ _ \| '_ \| __/ _ \ __/ _ \ / _ \ |
#      \  /\  /  __/ | (_| (_) | | | | | |  __/ | || (_) | | | | (_) | | | | ||  __/ || (_) |  __/_|
#       \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/  |_|  \___/|_| |_|\__\___|\__\___/ \___(_)
#
#
# Tic Tac Toe using Loops, funtions, lists, and the min-max algorithm

import os
import random

# Defining the board
# Tic-tac-toe 3x3
dimension = 3
#[layer][row][column]
my_board = [[[' ' for col in range(dimension)] for col in range(dimension)] for row in range(dimension)]



#Condition to win in 2D
def win2D(symbol):
    if ( (my_board[0][0][0] == my_board[0][1][0] == my_board[0][2][0] == symbol)  # Flat Horizontal
    or (my_board[0][0][1] == my_board[0][1][1] == my_board[0][2][1] == symbol)  # Flat Horizontal
    or (my_board[0][0][2] == my_board[0][1][2] == my_board[0][2][2] == symbol)  # Flat Horizontal
    or (my_board[1][0][0] == my_board[1][1][0] == my_board[1][2][0] == symbol)  # Flat Horizontal
    or (my_board[1][0][1] == my_board[1][1][1] == my_board[1][2][1] == symbol)  # Flat Horizontal
    or (my_board[1][0][2] == my_board[1][1][2] == my_board[1][2][2] == symbol)  # Flat Horizontal
    or (my_board[2][0][0] == my_board[2][1][0] == my_board[2][2][0] == symbol)  # Flat Horizontal
    or (my_board[2][0][1] == my_board[2][1][1] == my_board[2][2][1] == symbol)  # Flat Horizontal
    or (my_board[2][0][2] == my_board[2][1][2] == my_board[2][2][2] == symbol)  # Flat Horizontal

    or (my_board[0][0][0] == my_board[0][0][1] == my_board[0][0][2] == symbol)  # Flat Vertical
    or (my_board[0][1][0] == my_board[0][1][1] == my_board[0][1][2] == symbol)  # Flat Vertical
    or (my_board[0][2][0] == my_board[0][2][1] == my_board[0][2][2] == symbol)  # Flat Vertical
    or (my_board[1][0][0] == my_board[1][0][1] == my_board[1][0][2] == symbol)  # Flat Vertical
    or (my_board[1][1][0] == my_board[1][1][1] == my_board[1][1][2] == symbol)  # Flat Vertical
    or (my_board[1][2][0] == my_board[1][2][1] == my_board[1][2][2] == symbol)  # Flat Vertical
    or (my_board[2][0][0] == my_board[2][0][1] == my_board[2][0][2] == symbol)  # Flat Vertical
    or (my_board[2][1][0] == my_board[2][1][1] == my_board[2][1][2] == symbol)  # Flat Vertical
    or (my_board[2][2][0] == my_board[2][2][1] == my_board[2][2][2] == symbol)  # Flat Vertical

    or (my_board[0][0][0] == my_board[0][1][1] == my_board[0][2][2] == symbol)  # Flat Diagonal
    or (my_board[1][0][0] == my_board[1][1][1] == my_board[1][2][2] == symbol)  # Flat Diagonal
    or (my_board[2][0][0] == my_board[2][1][1] == my_board[2][2][2] == symbol)  # Flat Diagonal
    or (my_board[0][0][2] == my_board[0][1][1] == my_board[0][2][0] == symbol)  # Flat Diagonal
    or (my_board[1][0][2] == my_board[1][1][1] == my_board[1][2][0] == symbol)  # Flat Diagonal
    or (my_board[2][0][2] == my_board[2][1][1] == my_board[2][2][0] == symbol) ):  # Flat Diagonal
        return True
    return False


#Condition to win in 3D
def win3D(symbol):
    if ( (my_board[0][0][0] == my_board[1][0][0] == my_board[2][0][0] == symbol)  # 3D Tower 0
    or (my_board[0][1][0] == my_board[1][1][0] == my_board[2][1][0] == symbol ) # 3D Tower 1
    or (my_board[0][2][0] == my_board[1][2][0] == my_board[2][2][0] == symbol)  # 3D Tower 2
    or (my_board[0][0][1] == my_board[1][0][1] == my_board[2][0][1] == symbol)  # 3D Tower 3
    or (my_board[0][1][1] == my_board[1][1][1] == my_board[2][1][1] == symbol)  # 3D Tower 4
    or (my_board[0][2][1] == my_board[1][2][1] == my_board[2][2][1] == symbol)  # 3D Tower 5
    or (my_board[0][0][2] == my_board[1][0][2] == my_board[2][0][2] == symbol)  # 3D Tower 6
    or (my_board[0][1][2] == my_board[1][1][2] == my_board[2][1][2] == symbol)  # 3D Tower 7
    or (my_board[0][2][2] == my_board[1][2][2] == my_board[2][2][2] == symbol)  # 3D Tower 8

    or (my_board[0][0][0] == my_board[1][0][1] == my_board[2][0][2] == symbol)  # 3D Vertical Diagonal
    or (my_board[2][0][0] == my_board[1][0][1] == my_board[0][0][2] == symbol)  # 3D Vertical Diagonal
    or (my_board[0][1][0] == my_board[1][1][1] == my_board[2][1][2] == symbol)  # 3D Vertical Diagonal
    or (my_board[2][1][0] == my_board[1][1][1] == my_board[0][1][2] == symbol)  # 3D Vertical Diagonal
    or (my_board[0][2][0] == my_board[1][2][1] == my_board[2][2][2] == symbol)  # 3D Vertical Diagonal
    or (my_board[2][2][0] == my_board[1][2][1] == my_board[0][2][2] == symbol)  # 3D Vertical Diagonal

    or (my_board[0][0][0] == my_board[1][1][0] == my_board[2][2][0] == symbol)  # 3D Horizontal Diagonal
    or (my_board[2][0][0] == my_board[1][1][0] == my_board[0][2][0] == symbol)  # 3D Horizontal Diagonal
    or (my_board[0][0][1] == my_board[1][1][1] == my_board[2][2][1] == symbol)  # 3D Horizontal Diagonal
    or (my_board[2][0][1] == my_board[1][1][1] == my_board[0][2][1] == symbol)  # 3D Horizontal Diagonal
    or (my_board[0][0][2] == my_board[1][1][2] == my_board[2][2][2] == symbol)  # 3D Horizontal Diagonal
    or (my_board[2][0][2] == my_board[1][1][2] == my_board[0][2][2] == symbol)  # 3D Horizontal Diagonal

    or (my_board[0][0][0] == my_board[1][1][1] == my_board[2][2][2] == symbol)  # 3D Cross Diagonal
    or (my_board[2][0][0] == my_board[1][1][1] == my_board[0][2][2] == symbol)  # 3D Cross Diagonal
    or (my_board[0][0][2] == my_board[1][1][1] == my_board[2][2][0] == symbol)  # 3D Cross Diagonal
    or (my_board[0][2][0] == my_board[1][1][1] == my_board[2][0][2] == symbol) ):  # 3D Cross Diagonal
        return True
    return False

def printHeader():
    print('------------------------ Welcome to Fontetoe ------------------------')
    print('                         Your 3D Tic-Tac-Toe                         ')



def playerOne():
    pos = 20
    print('Player One Turn: ')
    while( pos not in range (1, 10) ):
        pos = input('Please enter position you want to put X (1-9): ')
        try:
            pos = int(pos)
        except:
            print('', end ='')
    pos = pos - 1
    if isEmptyLayerOne(pos):
        insertX(0, pos)
        return True
    elif isEmptyLayerTwo(pos):
        insertX(1, pos)
        return True
    elif isEmptyLayerThree(pos):
        insertX(2, pos)
        return True
    return False # All full

def playerTwo():
    pos = 20
    print('Player Two Turn: ')
    while( pos not in range (1, 10) ):
        pos = input('Please enter position you want to put O (1-9): ')
        try:
            pos = int(pos)
        except:
            print('', end ='')
    pos = pos - 1
    if isEmptyLayerOne(pos):
        insertO(0, pos)
        return True
    elif isEmptyLayerTwo(pos):
        insertO(1, pos)
        return True
    elif isEmptyLayerThree(pos):
        insertO(2, pos)
        return True
    return False # All full

def my_AI():
    pos = random.randint(1,9)
    print('AI\'s move is', pos)
    pos = pos - 1
    if isEmptyLayerOne(pos):
        insertO(0, pos)
        return True
    elif isEmptyLayerTwo(pos):
        insertO(1, pos)
        return True
    elif isEmptyLayerThree(pos):
        insertO(2, pos)
        return True
    return False # All full

def insertX(layer, pos):
    my_board[layer][pos//3][pos%3] = 'X'

def insertO(layer, pos):
    my_board[layer][pos//3][pos%3] = 'O'

def isEmptyLayerOne(pos):
    #pos is from 0 - 8 but user chooses from 1 - 9
    row = pos//3
    col = pos % 3
    if(my_board[0][row][col] == ' '):
        return True
    return False

def isEmptyLayerTwo(pos):
    #pos is from 0 - 8 but user chooses from 1 - 9
    row = pos//3
    col = pos % 3
    if(my_board[1][row][col] == ' '):
        return True
    return False

def isEmptyLayerThree(pos):
    #pos is from 0 - 8 but user chooses from 1 - 9
    row = pos//3
    col = pos % 3
    if(my_board[2][row][col] == ' '):
        return True
    return False

def isFull():
    emptySpace = 0
    for i in my_board:
        for j in i:
            for k in j:
                if k == ' ':
                    emptySpace += 1

    if emptySpace > 1:  # Since we always have one blank element in board we must use > 1
        return False
    return True

def PvPmode():
    while( (not isFull()) ):
        # ---------------- Player one turn ----------------
        os.system('cls')
        printHeader()
        printBoard()
        while ( (not playerOne()) ):
            print('')

        if ( win2D('X') ):
            return 'Player One Wins'
        elif( win3D('X') ):
            return 'Player One Wins'

        # ---------------- Player two turn ----------------
        os.system('cls')
        printHeader()
        printBoard()
        while ( (not playerTwo()) ):
            print('')

        if ( win2D('O') ):
            return 'Player Two Wins'
        elif( win3D('O') ):
            return 'Player Two Wins'

    return 'Board full'

def AImode():
    while( (not isFull()) ):
        # ---------------- Player turn ----------------
        os.system('cls')
        printHeader()
        printBoard()
        while ( (not playerOne()) ):
            print('')

        if ( win2D('X') ):
            return 'Player One Wins'
        elif ( win3D('X') ):
            return 'Player One Wins'


        # ---------------- AI turn ----------------
        os.system('cls')
        printHeader()
        printBoard()
        while ( (not my_AI()) ):
            print('')

        if ( win2D('O') ):
            return 'AI Wins'
        elif( win3D('O') ):
            return 'AI Wins'

    return 'Board full'

def printBoard():
    count = 0
    for i in my_board:
        count += 1
        print('Layer ' + str(count), end='')
        for j in i:
            print('')
            for k in j:
                print(k + '|', end='')
        print('')
        print('')

def main():
    printHeader()
    userChoice = 'random'
    while (userChoice not in ['1', '2']):
        userChoice = input('Please choose your mode:\n1. Player vs Player\n2. Player vs AI\n')

    indicator = ''
    if(userChoice == '1'):
        indicator = PvPmode()
    elif(userChoice == '2'):
        indicator = AImode()
    return indicator

if __name__ == "__main__":
    print(main())
    print('Final Board: ')
    printBoard()


