import threading
import copy

class Board():
	player_pos_x = 0
	player_pos_y = 0
	solved = False
	tales_cpy = 0

	def __init__(self, board):
		self.board = board

	def print_board_str(self):
		index_vert = 0
		index_hor = 0
		string = "\n"

		string += ("-" * 25) + "\n"
		for row in self.board:
			index_hor += 1
			for i in row :
				if index_vert % 3 == 0 :
					string += "| "
				string += str(i) + " "
				index_vert+= 1 
			string += "| \n"
			if index_hor % 3 == 0 :
				string += ("-" * 25) + "\n"
		print(string, flush=False) #For the input while playing to work, i need to flush the stdout

	# def play_sudoku(self):
