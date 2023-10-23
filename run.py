from random import randint

print("Welcome")

def lets_start():
    """
    Gives the player a start the mission question.
    """  
    while True:
        play = input("Would you like to start comander 'Y' or 'N'?").upper()
        if play == 'Y':
            print("Excellent Commander. Good Luck!")
            break
        elif play == 'N':
            print("Sorry to hear that commander. Maybe next time.")
        else:
            print("Invalid input. Please try again with only 'Y' & 'N'!!!")
        
lets_start()


board = []

for x in range(0, 8,):
    board.append(['o'] * 8)

def print_board(board):
    """
    This is for the aesthetics of the game.
    Making nice rows for the user.
    """
    for row in board:
        print(' '.join(row))

print_board(board)

#   Still need to figure out how to change the indexes for user 
#  def index_board(board):
#     """
#     Change the index start number so the user can use the traditional 1 - 8
#     choices.
#     """
#     rows = [o, o , o, o, o, o, o, o]
#     for index, row in enumerate(rows, start=1):
#         return

# index_board(board)

def random_row(board):
    """
    This gives a random number on the row which will essentially
    be our 'Hidden ship'. Regardless of the size of the board.
    """
    return randint(0, len(board) -1)

def random_col(board):
    """
    This gives a random number on the column which will essentially
    be our 'Hidden ship'. Regardless of the size of the board.
    """
    return randint(0, len(board) -1)


bship_row = random_row(board)
bship_col = random_col(board)
# Delete these prints after testing and undo comment down below
print(bship_row)
print(bship_col)
guess_row = int(input("Guess Row: "))
guess_col = int(input("Guess Col: "))
print()

# print(bship_row)
# print(bship_col)


# Need to fix this function when you shoot out of range.
def correct_guess():
    """
    When player gets a correct guess a message will appear.
    """
    if guess_row == bship_row and guess_col == bship_col:
        print("BOOM!!! That was a Great hit!\n")
        else if guess_row < 8 and guess_col < 8:
            print("ddfddf")

            else:
            print("Ah you missed!!! You need to improve your aim!!!\n")
            board[guess_row][guess_col] = 'X'
            print_board(board)

correct_guess()

# def lets_start():
#     """
#     Gives the player a start the mission question.
#     """  
#     while True:
#         play = input("Would you like to start comander 'Y' or 'N'?").upper()
#         if play == 'Y':
#             print("Excellent Commander. Good Luck!")
#             break
#         elif play == 'N':
#             print("Sorry to hear that commander. Maybe next time.")
#         else:
#             print("Invalid input. Please try again with only 'Y' & 'N'!!!")
        
# lets_start()

# Might need to be before correct guess function
# def land_guess():
#     """
#     When player guesses out of range of the board a message will appear.
#     """
#     if guess_row != range(0,8) and guess_col != range(0,8):
#             print("Oh no, you have hit DRY LAND!!! Please try again!!")
#             print("Anywhere between 1 & 8 \n")

# land_guess()

# if board[guess_row][guess_col] == 'X':
#         print("You have hit me twice!")
