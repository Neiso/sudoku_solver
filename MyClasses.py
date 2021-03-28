import copy

class Board():
	def __init__(self, board):
		self.board = board
		self.board_init = copy.deepcopy(board)
		self.player_pos_x = 0
		self.player_pos_y = 0
		self.solved = False
		self.tales_cpy = 0
		self.correct = True

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
		
	"""
		Verify axes and board both verify if a value could fit in the board. If it can't, they return False and the solver
		Try to fit in an other value
	"""

	def verify_axes(self, x, y, value):
		for i in self.board[y]:
			if i == value:
				return 0
		for i in self.board:
			if i[x] == value:
				return 0
		return 1

	def verify_square(self, x, y, value):
		# 	y-= 2
		x -= x % 3
		y -= y % 3
		for i in self.board[y:y+3]:
			for j in i[x:x+3]:
				if j == value :
					return 0
		return 1

	"""	
		The solver find zero, if it finds one, it inserts a value starting from 1 through 9. After putting a value in, it launches the solver with the new board.
		It finds a zero again and try to fit a value. If in the new board, none of the 9 values could fit, in returns 0. It means that the initial value wasn't good so it tries
		with the upper value and restart again.
	"""
	def solver(self):
		x = 0
		y = 0
		for row in self.board:
			for i in row:
				if i == 0:
					for value in range(1,10):
						if (self.verify_square(x, y, value) and self.verify_axes(x, y, value)):
							row[x] = value
							if (self.solver()):
								return 1
							else:
								row[x] = 0
					if row[x] == 0:
						return 0
				x += 1
			x = 0
			y += 1
		return 1
				 
