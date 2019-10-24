# game board
board = [ ['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_'] ]

# current player is a STRING containing 'X'
current_player = 'X'

# winner is always FALSE (until it's not)
winner = False


filled_spaces = 0
endgame = False
valid_move = True

# Print the board when game starts
print("\nThis is a Human vs Human TicTacToe game, Player X vs Player O.")

def game_over():
    global endgame
    if current_player == 'X':
        print("The winner is Player X. Game over.")
        endgame = True
        
    elif current_player == 'O':
        print("The winner is Player O. Game over.")
        endgame = True

        

def check_win():
    if board[0][0] == board[0][1] and board[0][1] == board[0][2] and board[0][0] == board[0][2] and not board[0][0] == '_':
        game_over()


    elif board[1][0] == board[1][1]  and  board[1][1] == board[1][2]  and  board[1][0] == board[1][2]  and not board[1][0] == '_':
        game_over()


    elif  board[2][0] == board[2][1]  and  board[2][1] == board[2][2]  and  board[2][0] == board[2][2] and not board[2][0] == '_':
        game_over()

    
    elif board[0][0] == board[1][0]  and  board[1][0] == board[2][0]  and  board[0][0] == board[2][0]  and not board[0][0] == '_':
        game_over()


    elif  board[0][1] == board[1][1]  and board[1][1] == board[2][1] and  board[0][1] == board[2][1]  and not board[0][1] == '_':
        game_over()
 

    elif board[0][2] == board[1][2] and  board[1][2] == board[2][2]  and  board[0][2] == board[2][2]  and not board[0][2] == '_':
        game_over()


    elif  board[0][0] == board[1][1]  and board[1][1] == board[2][2]  and  board[0][0] == board[2][2]  and not board[0][0] == '_':
        game_over()

    elif  board[0][2] == board[1][1] and  board[1][1] == board[2][0]  and  board[0][2] == board[2][0]  and not board[0][2] == '_':
        game_over()




def summon_board():
    for rows in board:
        print(rows)

summon_board()


print("\nPlayer X will start first.\nPlease choose the cell in which you want to fill in, \nby giving us row number followed by the column number.\n ")




while ( filled_spaces < 9) and (endgame == False):
    while True:
        row_number = input("")
        # Permissible row numbers: 1, 2 and 3 only.
        if ( (row_number == "1") or (row_number == "2") or (row_number == "3")):
            break
        else:
            print("The only possible input for the row numbers are 1, 2 and 3. Try again.")

    while True:
        column_number = input("")
        # Permissible column numbers: 1, 2 and 3 only.
        if ( (column_number == "1") or (column_number == "2") or (column_number == "3")):
            break
        else:
            print("The only possible input for the column numbers are 1, 2 and 3. Try again.")
    
    # check if it's a valid move
    if not(board[int(row_number) - 1][int(column_number) - 1] == '_'):
        print("This is an invalid move.\nSomeone has already filled in the position.\nPlease resubmit your coordinates.")
        valid_move = False
    else: 
        valid_move = True

    # updates and prints the board, then change the players' turn
    if current_player == 'X' and valid_move == True:
        board[int(row_number) - 1][int(column_number) - 1] = 'X'
        current_player = 'O'
        print("The board has now been updated. It is now Player O's turn.")
        filled_spaces += 1
        check_win()
        summon_board()

    elif current_player == 'O' and valid_move == True:
        board[int(row_number) - 1][int(column_number) - 1] = 'O'
        current_player = 'X'
        print("The board has now been updated. It is now Player X's turn.")
        filled_spaces += 1
        check_win()
        summon_board()
    
    if endgame == True:
        break
    else:
        print()



# check for draw scenario
while ((endgame == False) and (filled_spaces == 9)):
    print("This is a draw. There is no winners. Only losers!")
    break

# check for winning conditions
""" Winning conditions are:
    [0][0] [0][1] [0][2]
    [1][0] [1][1] [1][2]
    [2][0] [2][1] [2][2]
    [0][0] [1][0] [2][0]
    [0][1] [1][1] [2][1]
    [0][2] [1][2] [2][2]
    [0][0] [1][1] [2][2]
    [0][2] [1][1] [2][0]
"""




"""
git clone git@github.com:nahiphog/challenge-fswd-python-tic-tac-toe.git
"""




















# # function to print board each time we enter an 'X' or an 'O'
# def print_board():
#     for rows in board:
#         print(rows)

# # If current player is 'X' then next will be 'O' or else it will be 'X'


# def change_player():
#     if current_player == 'X':
#         return 'O'
#     return 'X'

# # check if board[x][y] contains a '_'


# def empty_space(x, y):
#     if board[x][y] == '_':
#         return True
#     return False


# # While there is no winner...
# while not winner:
#   # inputting your x and y coordinates for board[x][y]
#     x = int(input("Enter your x coordinate between 1-3 \n")) - 1
#     y = int(input("Enter your y coordinate between 1-3 \n")) - 1

#     # check if there is an empty space
#     # change the board[x][y] to X or O
#     # check winner
#     # check if there is a draw

# #################

