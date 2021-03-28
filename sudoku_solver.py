#!/usr/bin/python3

from os import system
from copy import deepcopy
from MyClasses import Board
from multiprocessing import Process
from time import sleep
from getch import getch

"""
	Print the board and next to it the board solved. Storing everything in a buffer makes it faster.
"""
def print_boards(board, board_cpy):
	string = "\n"
	for y in range(0, 9):
		if y % 3  == 0 :
			string += "-" * 25 + " " * 11 + "-" * 25 + "\n"
		for x in range(0, 9):
			if x % 3  == 0 :
				string += "| "
			string += str(board[y][x]) + " "
		string += "| "
		if y == 4 :
			string += (" " * 3 + "->" + " " * 5)
		else:
			string += (" " * 10)
		for x in range(0, 9):
			if x % 3  == 0 :
				string += ("| ")
			string += str(board_cpy[y][x]) + " "
		string += "| " + "\n"
	string += "-" * 25 + " " * 11 + "-" * 25 + "\n"
	print(string)

"""
	To play the sudoku, I had to make 2 processes. One for getting the input from the user and the other one to tell the player on which tale he is. I tried to use threading to share
	the same data so the thread could run in the back and when i would set the board object to be done, the thread would stop. But in order to get the input from the user without him pressing
	enter, i had to use a very high level sys call. This high level call would pause the process, so all the thread within got froze. So i used processing which is very slower and
	unhandy. Since it can't share data, the object don't get update in the second process so i have to kill it and relaunch it with the new user's input data. Which makes it very slow.
	I think there is a way to communicate between processes but that will be for an optimized version (v0.4). 
"""
def display_sudoku_highligth(board):
	system("clear")
	board.print_board_str(playing = True)
	print("Move around with QZSD and exit with X.", flush=True)
	sleep(0.05)
	x = board.player_pos_x
	y = board.player_pos_y
	board.tale_cpy = board.board[y][x]
	board.board[y][x] = " "
	swap = True
	system("clear")
	while (not board.solved):
		board.print_board_str(playing = True)
		print("Move around with QZSD and exit with X.", flush=True)
		sleep(0.35)
		if (swap):
			swap = False
			board.board[y][x] = board.tale_cpy
		else :
			swap = True
			board.board[y][x] = " "
		system("clear")

def play_sudoku(board):
	x = 0
	y = 0
	while (not board.solved):
		board.tales_cpy = board.board[x][y]
		my_process = Process(target=display_sudoku_highligth, args=[board])
		my_process.start()
		string = getch()
		my_process.terminate()
		sleep(0.033)
		if string == 'q':
			if board.board[y][x] == " ":
				board.board[y][x] = board.tales_cpy
			if (x == 0):
				x = 8
			else :
				x -= 1
			board.player_pos_x = x
			board.tales_cpy = board.board[y][x]
		elif string == 'd':
			if board.board[y][x] == " ":
				board.board[y][x] = board.tales_cpy
			if (x == 8):
				x = 0
			else :
				x += 1
			board.player_pos_x = x
			board.tales_cpy = board.board[y][x]
		elif string == 'z':
			if board.board[y][x] == " ":
				board.board[y][x] = board.tales_cpy
			if (y == 0):
				y = 8
			else :
				y -= 1
			board.player_pos_y = y
			board.tales_cpy = board.board[y][x]
		elif string == 's':
			if board.board[y][x] == " ":
				board.board[y][x] = board.tales_cpy
			if (y == 8):
				y = 0
			else :
				y += 1
			board.player_pos_y = y
			board.tales_cpy = board.board[y][x]
		elif (string in "0123456789") and (board.board_init[y][x] == 0):
			board.board[y][x] = int(string)
		elif string == 'x':
			break
	my_process.terminate()
	system("clear")
	board.is_valid_solution()

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
		system("clear")
		print(err, "\n")
		return init_board
	except ValueError as err:
		system("clear")
		print(err, "\n")
		return init_board

def menu():
	board_demo = [
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
	board = Board(board_demo)
	board_cpy = deepcopy(board)
	system("clear")
	while (True):
		print("\t\tWelcome to the Sudoku Solver v0.2\n")
		print("Choose an option :\n")
		print("1]\tPrint the board")
		print("2]\tTry to solve it")
		print("3]\tDisplay the solution")
		print("4]\tImport a board")
		print("5]\tQuit")
		raw_choice = input("\nYour choice : ")
		system("clear")
		if (raw_choice == "1"):
			board.print_board_str()
		elif (raw_choice == "2"):
			play_sudoku(board)
			if board.correct:
				print ("Well done !\n")
		elif (raw_choice == "3"):
			board_cpy.solver()
			print_boards(board.board, board_cpy.board)
		elif (raw_choice == "4"):
			system("clear")
			board = import_board(board)
			board_cpy = deepcopy(board)
		elif (raw_choice == "5" or raw_choice == "exit"):
			break
		else :
			print("Enter a proper value please.\n")
		sleep(0.5)
                

#avoid running code in import
if __name__ == "__main__":
	menu()
