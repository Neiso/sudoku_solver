

def print_board(board):
	index_vert = 0
	index_hor = 0

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



def main():
	board = [
		[0, 0, 0, 0, 0, 0, 0, 7, 0],
		[0, 0, 0, 0, 5, 0, 8, 0, 1],
		[0, 0, 6, 4, 1, 0, 0, 3, 5],
		[6, 0, 7, 0, 0, 0, 5, 2, 0],
		[0, 0, 0, 2, 0, 9, 0, 0, 0],
		[0, 4, 1, 0, 0, 0, 6, 0, 9],
		[9, 7, 0, 0, 2, 1, 4, 0, 0],
		[1, 0, 5, 0, 3, 0, 0, 0, 0],
		[0, 8, 0, 0, 0, 0, 0, 0, 0]
	]
	print_board(board)

main()