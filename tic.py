import os

board = ["-", "-", "-", 
	 	 "-", "-", "-", 
	     "-", "-", "-" ]

chance = "X"
winner = None
win = 0
count = 0


#displaying the board		 
def display_board():

	os.system('clear')

	print(board[0] + " | " + board[1] + " | " + board[2])
	print(board[3] + " | " + board[4] + " | " + board[5])
	print(board[6] + " | " + board[7] + " | " + board[8])


display_board()


def play_game():	

	#playing the turn
	turn()

	#switching to next player
	switch_player()

	#checking row, col and diagonal
	check_win()

	#checking if game is still on
	game_active()

	
#playing the turn
def turn():

	#position input
	position = input("Enter the position (1-9) : ")
	position = int(position) - 1


	#making sure the position is available
	if(board[position] == "-"):

		#print at the selected position
		board[position] = chance

	else:

		print("This position is already occupied! Try again.")
		play_game()

	display_board()

		

#switching to next player
def switch_player():

	global chance

	if chance == "O":
		chance = "X"
	else:
		chance = "O"


#checking if board is full
def game_active():
	
	global count

	if(win >0):
		print_winner()

	else:
		
		for x in range(0, 9):
	
			if (board[x] == "-"):
				count += 1
				
				#if atleast one place is empty
				if count != 9:
					print(count)
					play_game()

				print_winner()




def check_win():

	check_row()
	check_col()
	check_diag()



def check_row():

	global winner, win

	if(board[0] == board[1] and board[1] == board[2] != "-"):
		win += 1
		if(board[0] == "X"):
			winner = "X"
		elif(board[0] == "O"):
			winner = "O"

	elif(board[3] == board[4] and board[4] == board[5] != "-"):
		win += 1
		if(board[3] == "X"):
			winner = "X"
		elif(board[3] == "O"):
			winner = "O"

	elif(board[6] == board[7] and board[7] == board[8] != "-"):
		win += 1
		if(board[6] == "X"):
			winner = "X"
		elif(board[6] == "O"):
			winner = "O"

	else:
		return None

	return winner

def check_col():
	
	global winner, win

	if(board[0] == board[3] and board[3] == board[6] != "-"):
		win += 1
		if(board[0] == "X"):
			winner = "X"
		elif(board[0] == "O"):
			winner = "O"

	elif(board[1] == board[4] and board[4] == board[7] != "-"):
		win += 1
		if(board[1] == "X"):
			winner = "X"
		elif(board[1] == "O"):
			winner = "O"

	elif(board[2] == board[5] and board[5] == board[8] != "-"):
		win += 1
		if(board[2] == "X"):
			winner = "X"
		elif(board[2] == "O"):
			winner = "O"

	else:
		return None

	return winner

def check_diag():
	
	global winner, win

	if(board[0] == board[4] and board[4] == board[8] != "-"):
		win += 1
		if(board[0] == "X"):
			winner = "X"
		elif(board[0] == "O"):
			winner = "O"

	elif(board[2] == board[4] and board[4] == board[6] != "-"):
		win += 1
		if(board[6] == "X"):
			winner = "X"
		elif(board[6] == "O"):
			winner = "O"

	else:
		return None

	return winner


def print_winner():
	if(winner == "X" or winner =="O"):
		print(winner + "Wins!")

	else:
		print("Tie!")

	exit(0)
	

play_game()