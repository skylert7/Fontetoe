#Tic Tac Toe using Loops, funcitons, lists, and the min-max algorithm

import os
import time
import random

#Defining the board
board = [" " for x in range(10)]

def printHeader():
	print """ Welcome to Tic Tac Toe!"""



def insertLetter(letter, pos):
	board[pos] = letter

def spaceIsFree(pos):
	return board[pos] == ' '

def printBoard(board):
	print(' |  | ')
	print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
	print(' |  | ')
	print('-----------')
	print(' |  | ')
	print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
	print(' |  | ')
	print('-----------')
	print(' |  | ')
	print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
	print(' |  | ')


def isWin(bo, le):
	return (bo[7] == le and bo [8] == le and bo == [9]) or
	(bo[4] == le and bo[5] == le and bo[6] == le) or
	

def compMove():
	pass


def selectRandom(board):
	pass

def isFull(board):
	pass

def main():
	pass


main()




