import os
from random import randint


global guess_row
global guess_col
global bship_col
global bship_row
global game_active
global guesses


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
    global game_active
    global guesses

    while True:
        play = input("Would you like to start comander 'Y' or 'N'?").upper()
        clear()
        if play == 'Y':
            print("Excellent Commander. Good Luck!")
            game_active = True
            guesses = 0
            break
        elif play == 'N':
            print("Sorry to hear that commander. Maybe next time.")
            game_active = False
            break
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


def random_num(board):
    """
    This gives a random number on the row/col which will essentially
    be our 'Hidden ship'. Regardless of the size of the board.
    """
    return randint(0, len(board) - 1)


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


def place_ship():
    """
    This function keeps the ship in just one area of the grid
    """
    global bship_col
    global bship_row

    bship_col = random_num(board) 
    bship_row = random_num(board)
# Add extra ships!!!!
# for i in range(2):
    
place_ship()


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
            guess_row = int(guess_row) 
            break

    while True:
        guess_col = input("Guess Col: ")
        if validate_num(guess_col):
            guess_col = int(guess_col)
            break


def correct_guess():
    """
    When player guesses the player will get a correct message 
    according to whether the player has hit, missed, or over shot.
    """
    global guess_row
    global guess_col
    global game_active
    global guesses

    if guess_row == bship_row and guess_col == bship_col:
        board[bship_row][bship_col] = '@'
        print_board(board)
        print("BOOM!!! That was a Great hit!\n")
        game_active = False
    
    elif guess_row not in range(8) or guess_col not in range(8):
        print("you are hitting land try again\n")

    elif board[guess_row][guess_row] == 'X':
        print("You have hit me before!!!")

    else:
        guesses = guesses + 1
        print("Ah you missed!!! You need to improve your aim!!!\n")
        board[guess_row][guess_col] = 'X'
        print_board(board)


def game():
    """
    This function allows the user to a have limited amount of guesses before 
    the game ends.
    """
    global bship_col
    global bship_row
    global game_active
    global guesses

    while guesses < 4:
        # Delete these prints after testing and undo comment down below
        print(bship_row)
        print(bship_col)
        if game_active:
            user_guess()

            print()

            correct_guess()
        else:
            break
    if guesses <= 4 and game_active:
        print("Game over, No more guesses")
    if not game_active:
        print(f"Congratulations, You guessed it in {guesses + 1} guesses")
        

game()    

# global guess_row
#     global guess_col
#     global game_active
#     global guesses

#     if guess_row == bship_row and guess_col == bship_col:
#         board[bship_row][bship_col] = '@'
#         print_board(board)
#         print("BOOM!!! That was a Great hit!\n")
#         game_active = False
    
#     elif board[guess_row][guess_row] == 'X':
#         print("You have hit me before!!!")

#     elif guess_row not in range(8) or guess_col not in range(8):
#         print("you are hitting land try again\n")
    
#     else:
#         guesses = guesses + 1
#         print("Ah you missed!!! You need to improve your aim!!!\n")
#         board[guess_row][guess_col] = 'X'
#         print_board(board)