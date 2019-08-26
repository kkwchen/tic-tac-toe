import random

# create the board
board = ['-']*9 

# print board state
def print_board(board):
    print(" ", "   ", "1", "   ","2", "   ","3")
    print("A", " | ", board[0], " | ", board[1], " | ", board[2])
    print("B", " | ", board[3], " | ", board[4], " | ", board[5])
    print("C", " | ", board[6], " | ", board[7], " | ", board[8])

# choose random position, check if there is an element there and place if empty
def get_guess(board, ai_symbol):
    i = 0
    while True:
        ai_choice = random.randint(0,8)
        if board[ai_choice] == '-':
            board[ai_choice] = ai_symbol
            return board
        i += 1

        # if the board is full and game has not ended, you tie
        if i > 8:
            print_board(board)
            print('Good Game! You Tied.')
            exit(0)

# check if win condition has been met
def check_win(board, player_mark):    
    for i in range(0,3):
        # columns
        if board[i] == board[i+3] == board[i+6] == player_mark:            
            print_board(board)
            print(player_mark, ' Wins!')
            exit(0)

        # rows
        row = i*3
        if board[row] == board[row+1] == board[row+2] == player_mark:
            print_board(board)
            print(player_mark, ' Wins!')
            exit(0)

    # diagonals
    if board[0] == board[4] == board[8] == player_mark or board[2] == board[4] == board[6] == player_mark:
        print_board(board)
        print(player_mark, ' Wins!')
        exit(0)


# get player X or O
print("Welcome to tic tac toe, please choose X's or O's. Type Quit at any time to exit.")
player_symbol = input()
intro = True

# assign comp the opposite symbol, check for valid input
while intro:
    if player_symbol == "Quit":
        exit(0)
    elif player_symbol.lower()  == 'x':
        ai_symbol = 'O'
        intro = False
    elif player_symbol.lower() == 'o':
        ai_symbol = 'X'
        intro = False
    else:
        print("Invalid Input")
        player_symbol = input()

print("You chose, ", player_symbol, " your opponent will be, ", ai_symbol)


# main game loop
while True:
    print_board(board)

    print("Type a Grid Location to place mark")

    # get location
    grid_location = input()

    # place symbol is corresponding array index
    if grid_location == 'A1':
        board[0] = player_symbol
        player_chose = True
    elif grid_location == 'A2':
        board[1] = player_symbol
        player_chose = True
    elif grid_location == 'A3':
        board[2] = player_symbol
        player_chose = True
    elif grid_location == 'B1':
        board[3] = player_symbol
        player_chose = True
    elif grid_location == 'B2':
        board[4] = player_symbol
        player_chose = True
    elif grid_location == 'B3':
        board[5] = player_symbol
        player_chose = True
    elif grid_location == 'C1':
        board[6] = player_symbol
        player_chose = True
    elif grid_location == 'C2':
        board[7] = player_symbol
        player_chose = True
    elif grid_location == 'C3':
        board[8] = player_symbol
        player_chose = True
    elif grid_location == "Quit":
        exit(0)
    else:
        print("Invalid Grid Location")
        player_chose = False
    
    # if the player has input a valid location, computer guesses randomly
    if player_chose:
        check_win(board, player_symbol)    

        board = get_guess(board, ai_symbol)

        check_win(board, ai_symbol)