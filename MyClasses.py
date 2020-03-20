import threading
import copy

class Board():
	def __init__(self, board):
		self.board = board
		self.board_init = copy.deepcopy(board)

	player_pos_x = 0
	player_pos_y = 0
	solved = False
	tales_cpy = 0
	correct = True


	def print_board_str(self, playing=False):
		index_vert = 0
		index_hor = 0
		string = "\n"

		string += ("-" * 25) + "\n"
		for row in self.board:
			index_hor += 1
			for i in row :
				if index_vert % 3 == 0 :
					string += "| "
				#If player made changes on the board, print his changes in blue.
				if (self.board_init[index_hor - 1][index_vert] != self.board[index_hor - 1][index_vert]):
					string += "\033[94m" + str(i) + "\033[0m "
				#Else if player hasn't made change, underline the position he stands on for better visualisation.
				elif (playing and self.player_pos_x == index_vert and self.player_pos_y == index_hor - 1):
					string += "\033[4m" + str(i) + "\33[0m "
				#Print other digits.
				else:
					string += str(i) + " "
				index_vert+= 1 
			index_vert = 0
			string += "| \n"
			if index_hor % 3 == 0 :
				string += ("-" * 25) + "\n"
		print(string, flush=True) #For the input while playing to work properly, i need to flush the stdout so it prints out instantly instrad of buffering the output

	def print_board_finished(self, liste):
		index_vert = 0
		index_hor = 0
		string = "\n"

		string += ("-" * 25) + "\n"
		for row in self.board:
			index_hor += 1
			for i in row :
				if index_vert % 3 == 0 :
					string += "| "
				if ((index_vert, index_hor - 1) in liste):
					string += "\033[91m" + str(i) + " \033[0m"
				else :
					string += str(i) + " "
				index_vert+= 1 
			index_vert = 0
			string += "| \n"
			if index_hor % 3 == 0 :
				string += ("-" * 25) + "\n"
		print(string, flush=True) #For the input while playing to work properly, i need to flush the stdout so it prints out instantly instrad of buffering the output

	def is_valid_solution(self):
		from sudoku_solver import verify_axes, verify_square
		mistakes = []
		player_board = self.board
		count = 0
		for y in range (0, 9):
			for x in range (0, 9):
				if (self.correct and player_board[y][x] == 0):
					self.correct = False
				if player_board[y].count(player_board[y][x]) != 1:
					mistakes.append((x, y))
		for x in range (0, 9):
			for y in range (0, 9):
				value = player_board[y][x]
				for i in range(0, 9):
					if (value == player_board[i][x]):
						count += 1
				if count > 1 and value != 0:
					mistakes.append((x, y))	
				count = 0
		if len(mistakes) > 0:
			self.correct = False
		else :
			self.correct = True
		mistakes.sort()
		index = 0
		for i in mistakes :
			index += 1
			while (mistakes.count(i) > 1):
				mistakes.pop(index)
		self.print_board_finished(mistakes)
		

				 
