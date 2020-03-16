import os
import copy

def print_boards(board, board_cpy):
	index_vert = 0
	index_hor = 0

	print("")
	print("-" * 25, " " * 10, "-" * 25)
	while (index_vert < 9):
		while (index_hor < 9):
			if index_hor % 3  == 0 :
				print("| ", end = "")
			print(str(board[index_vert][index_hor]) + " ", end="")
			index_hor += 1
		print("| ", end="")
		index_hor = 0
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

def print_board_str(board):
	index_vert = 0
	index_hor = 0
	string = "\n"

	string += ("-" * 25) + "\n"
	for row in board:
		index_hor += 1
		for i in row :
			if index_vert % 3 == 0 :
				string += "| "
			string += str(i) + " "
			index_vert+= 1 
		string += "| \n"
		if index_hor % 3 == 0 :
			string += ("-" * 25) + "\n"
	print(string)
	return (string)


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
	print("here")

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
	board_cpy = copy.deepcopy(board)
	os.system("clear")
	while (True):
		print("\t\tWelcome to the Sudoku Solver v0.2\n")
		print("Choose an option :\n")
		print("1]\tPrint the board")
		print("2]\tTry to solve it")
		print("3]\tDisplay the solution")
		print("4]\tQuit")
		raw_choice = input("\nYour choice : ")
		os.system("clear")
		if (raw_choice == "1"):
			print_board_str(board)
		elif (raw_choice == "2"):
			play_soduku(board_cpy)
		elif (raw_choice == "3"):
			solver(board_cpy)
			print_boards(board, board_cpy)
		elif (raw_choice == "4"):
			break
	print_boards(board, board_cpy)

menu()