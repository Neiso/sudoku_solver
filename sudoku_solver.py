#!/usr/bin/python3

import os
import copy
from MyClasses import Board
import threading
import multiprocessing
import time
import getch

def print_boards(board, board_cpy):
	index_vert = 0
	index_hor = 0

	print("")
	print("-" * 25 + " " * 11 + "-" * 25)
	while (index_vert < 9):
		while (index_hor < 9):
			if index_hor % 3  == 0 :
				print("| ", end = "")
			print(str(board[index_vert][index_hor]) + " ", end="")
			index_hor += 1
		print("| ", end="")
		index_hor = 0
		if index_vert == 4 :
			print (" " * 3 + "->" + " " * 5, end="")
		else:
		 print(" " * 10, end="")
		while (index_hor < 9):
			if index_hor % 3  == 0 :
				print("| ", end = "")
			print(str(board_cpy[index_vert][index_hor]) + " ", end="")
			index_hor += 1
		index_hor = 0
		print("| ")
		index_vert += 1
		if index_vert % 3  == 0 :
			print("-" * 25 + " " * 10, "-" * 25)
	print("")

def verify_axes(board, x, y, value):
	for i in board[y]:
		if i == value:
			return 0
	for i in board:
		if i[x] == value:
			return 0
	return 1

def verify_square(board, x, y, value):
	if (x % 3 == 1):
		x -= 1
	elif (x % 3 == 2):
		x -= 2
	if (y % 3 == 1):
		y -= 1
	elif (y % 3 == 2):
		y-= 2
	for i in board[y:y+3]:
		for j in i[x:x+3]:
			if j == value :
				return 0
	return 1

def solver(board):
	x = 0
	y = 0
	for row in board:
		for i in row:
			if i == 0:
				for value in range(1,10):
					if (verify_square(board, x, y, value) and verify_axes(board, x, y, value)):
						row[x] = value
						if (solver(board)):
							return 1
						else:
							row[x] = 0
				if row[x] == 0:
					return 0
			x += 1
		x = 0
		y += 1
	return 1

def play_soduku(board):
	x = board.player_pos_x
	y = board.player_pos_y
	board.tale_cpy = board.board[y][x]
	board.board[y][x] = " "
	swap = True
	os.system("clear")
	while (not board.solved):
		board.print_board_str()
		if (swap):
			swap = False
			board.board[y][x] = board.tale_cpy
		else :
			swap = True
			board.board[y][x] = " "
		time.sleep(0.5)
		os.system("clear")

def valid_board(board):
	if (len(board) != 9):
		return (False)
	for row in board :
		if (len(row) != 9):
			return (False)
	return (True)

def import_board(init_board):
	try:	
		board = Board([])
		row = []
		print ("Insert each row of the sudoku board. for example : \n\t002060040\n")
		print ("If you made a mistake, you can go back like this at the end : \n\tgoto 4\n\t002060040\n")
		for i in range(0, 9):
			row_raw = input("Type the {} row in one line : ".format(i + 1))
			if (row_raw == "exit"):
				return(init_board)
			else :
				for index in row_raw:
					if index not in "0123456789":
						raise TypeError("Only digit.")
					row.append(int(index))
			board.board.append(row)
			row = []
		string = input("Type OK if you are done or goto to make changes or print the board : ")
		while(string.upper() != "OK"):
			if (string[0:4] == "goto"):
				row_index = int(string[5])
				string = input("Type the {} row in one line : ".format(int(string[5])))
				row = list(map(int, list(string)))
				board.board[row_index - 1] = row
			elif (string[0:5] == "print"):
				board.print_board_str()
			string = input("Type OK if you are done or goto to make changes or print the board : ")
		if (valid_board(board.board)):	
			return board
		else :
			raise ValueError("Not a proper Board")
	except TypeError as err:
		os.system("clear")
		print(err, "\n")
		return init_board
	except ValueError as err:
		os.system("clear")
		print(err, "\n")
		return init_board

def menu():
	board = [
		[3, 7, 0, 9, 2, 0, 8, 4, 0],
		[0, 1, 0, 0, 7, 0, 9, 0, 2],
		[2, 0, 0, 0, 0, 4, 0, 7, 0],
		[0, 3, 1, 0, 0, 5, 0, 0, 0],
		[0, 8, 7, 0, 0, 0, 3, 2, 0],
		[0, 0, 0, 7, 0, 0, 1, 6, 0],
		[0, 6, 0, 3, 0, 0, 0, 0, 8],
		[8, 0, 3, 0, 9, 0, 0, 5, 0],
		[0, 5, 4, 0, 6, 7, 0, 9, 3]
	]
	board = Board(board)
	board_cpy = copy.deepcopy(board.board)
	os.system("clear")
	while (True):
		print("\t\tWelcome to the Sudoku Solver v0.2\n")
		print("Choose an option :\n")
		print("1]\tPrint the board")
		print("2]\tTry to solve it")
		print("3]\tDisplay the solution")
		print("4]\tImport a board")
		print("5]\tQuit")
		raw_choice = input("\nYour choice : ")
		os.system("clear")
		if (raw_choice == "1"):
			board.print_board_str()
		# elif (raw_choice == "2"):
		# 	play_soduku(board_cpy)
		elif (raw_choice == "3"):
			solver(board_cpy)
			print_boards(board.board, board_cpy)
		elif (raw_choice == "4"):
			board = import_board(board)
			board_cpy = copy.deepcopy(board.board)
		elif (raw_choice == "5" or raw_choice == "exit"):
			break
		else :
			print("Enter a proper value please.\n")

# menu()

board = [
	[3, 7, 0, 9, 2, 0, 8, 4, 0],
	[0, 1, 0, 0, 7, 0, 9, 0, 2],
	[2, 0, 0, 0, 0, 4, 0, 7, 0],
	[0, 3, 1, 0, 0, 5, 0, 0, 0],
	[0, 8, 7, 0, 0, 0, 3, 2, 0],
	[0, 0, 0, 7, 0, 0, 1, 6, 0],
	[0, 6, 0, 3, 0, 0, 0, 0, 8],
	[8, 0, 3, 0, 9, 0, 0, 5, 0],
	[0, 5, 4, 0, 6, 7, 0, 9, 3]
]

board = Board(board)
x = 8
y = 8
board.player_pos_x = x
board.player_pos_y = y
board.tales_cpy = board.board[x][y]
thread1 = multiprocessing.Process(target=play_soduku, args=[board])
thread1.start()
while (not board.solved):
	string = getch.getch()
	if string == 'q':
		thread1.terminate()
		thread1 = multiprocessing.Process(target=play_soduku, args=[board])
		if board.board[x][y] == " ":
			board.board[x][y] = board.tales_cpy
		x -= 1
		board.player_pos_x = x
		board.tales_cpy = board.board[x][y]
		thread1.start()
	if string == 'x':
		break
thread1.terminate()
board.print_board_str()