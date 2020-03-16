import os

def print_board(board):
	index_vert = 0
	index_hor = 0

	print("")
	print("-" * 25)
	for row in board:
		index_hor += 1
		for i in row :
			if index_vert % 3 == 0 :
				print("| ", end = "")
			print(i, "", end="")
			index_vert+= 1 
		print("| ")
		if index_hor % 3 == 0 :
			print("-" * 25)
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

def solver(board, x=0, y=0):
	x = 0
	y = 0
	for row in board:
		for i in row:
			if i == 0:
				for value in range(1,10):
					if (verify_square(board, x, y, value) and verify_axes(board, x, y, value)):
						row[x] = value
						if (solver(board, x, y)):
							return 1
						else:
							row[x] = 0
				if row[x] == 0:
					return 0
			x += 1
		x = 0
		y += 1
	return 1

def main():
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
	# print_board(board)
	solver(board)
	# print_board(board)
	with open("result.txt", "w") as f:
		f.write(print_board_str(board))
	os.system("diff solved.txt result.txt")

main()