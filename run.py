import os
from random import randint


global guess_row
global guess_col


def clear():
    """
    Clear function to clean-up the terminal so things don't get messy.
    """
    os.system("cls" if os.name == "nt" else "clear")


clear()
print("Welcome")

def lets_start():
    """
    Gives the player a start the mission question.
    """  
    while True:
        play = input("Would you like to start comander 'Y' or 'N'?").upper()
        clear()
        if play == 'Y':
            print("Excellent Commander. Good Luck!")
            break
        elif play == 'N':
            print("Sorry to hear that commander. Maybe next time.")
        else:
            print("Invalid input. Please try again with only 'Y' & 'N'!!!")
        
lets_start()


board = []

for x in range(0, 8):
    board.append(['o'] * 8)

def print_board(board):
    """
    This is for the aesthetics of the game.
    Making nice rows for the user.
    """
    for row in board:
        print(' '.join(row))

print_board(board)


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


def validate_num(num):
    """
    If user does not use a number as a guess this error message will
    appear
    """
    try:
        guess = int(num)
        return guess
    except ValueError:
        print(f"{num} Is not a valid number")


def user_guess():
    """
    The player inputs their guess here between 1 - 8. 
    This function changes the start of the indexes.
    """
    global guess_row
    global guess_col

    while True:
        guess_row = input("Guess Row: ")
        if validate_num(guess_row):
            guess_row = int(guess_row) - 1
            break

    while True:
        guess_col = input("Guess Col: ")
        if validate_num(guess_col):
            guess_col = int(guess_col) - 1
            break


bship_row = random_row(board)
bship_col = random_col(board)
# Delete these prints after testing and undo comment down below
print(bship_row)
print(bship_col)
user_guess()


print()

# print(bship_row)
# print(bship_col)


# Need to fix this function when you shoot out of range.
def correct_guess():
    """
    When player gets a correct guess a message will appear.
    """
    global guess_row
    global guess_col

    if guess_row == bship_row and guess_col == bship_col:
        print("BOOM!!! That was a Great hit!\n")
        
    else:
        print("Ah you missed!!! You need to improve your aim!!!\n")
        board[guess_row][guess_col] = 'X'
        print_board(board)

correct_guess()


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
