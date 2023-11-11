import os
import sys
from random import randint

global guess_row
global guess_col
global bship_col
global bship_row
global game_active
global guesses
global board


def clear():
    """
    Clear function to clean-up the terminal so things don't get messy.
    """
    os.system("cls" if os.name == "nt" else "clear")

clear()

print("Welcome To BATTLESHIPS!!!\n")
print("         /|")
print("        / |")
print("       /__|")
print("       __|__")
print("      \_____/\n")


def rules():

    while True:
        rule = input("Would you like to see the Rules? 'Y'/'N'")
        clear()
        if rule == 'Y':
            print("Rules!\n")
            print("This is a simple game please follow these rules Commander:")
            print("- Follow the instructions to get onto the mission board.")
            print("- There is only one Battleship on the board.")
            print("- You have four guesses to complete your mission.")
            print("- Choose a number between 0 and 4 for the row and column.")
            print("- No sleeping on duty.")
            print("Finally enjoy the game!\n")
            break
        else:
            rule == 'N'
            print("Excellent Commander!")
            break

rules()

        
def lets_start():
    """
    Gives the player the option to start the mission question or exit.
    """  
    global game_active
    global guesses

    while True:
        play = input("Would you like to start the mission Commander 'Y' or 'N'?\n").upper()
        clear()
        if play == 'Y':
            print("Excellent Commander. Good Luck!\n")
            game_active = True
            guesses = 0
            break
        elif play == 'N':
            print("Sorry to hear that Commander. Maybe next time.\n")
            game_active = False
            sys.exit()
        else:
            print("Invalid input. Please try again with only 'Y' & 'N'!!!\n")
                

def new_board():
    global board
    board = []

    for x in range(0, 5):
        board.append(['o'] * 5)


def print_board(board):
    """
    This is for the aesthetics of the game.
    Making a neat grid for the player.
    """
    for row in board:
        print(' '.join(row))
    
    print()


def random_num(board):
    """
    This gives a random number on the row/col which will essentially
    be the 'Hidden ship'. Regardless of the size of the board.
    """
    return randint(0, len(board) - 1)


def validate_num(num):
    """
    If player does not use a number as a guess this error message will
    appear.
    """
    if num.isdigit():
        return num
    else:
        print(f"{num} This is not a valid number")


def place_ship():
    """
    This function keeps the ship in just one area of the grid.
    """
    global bship_col
    global bship_row
    global board

    bship_col = random_num(board) 
    bship_row = random_num(board)


def user_guess():
    """
    The player inputs their guess here between 0 - 4. 
    This function changes the start of the indexes.
    """
    global guess_row
    global guess_col

    print()

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
    When player makes a guess the player will get a correct message 
    according to whether the player has hit, missed, or over shot.
    """
    global guess_row
    global guess_col
    global game_active
    global guesses
    global board

    clear()
    if guess_row == bship_row and guess_col == bship_col:
        board[bship_row][bship_col] = '@'
        print_board(board)
        print("BOOM!!! That was a Great hit!\n")
        game_active = False
    
    elif guess_row not in range(5) or guess_col not in range(5):
        print("You are hitting Dry Land!! Try Again\n")

    elif board[guess_row][guess_col] == 'X':
        print("You have hit me before!!!\n")

    else:
        guesses = guesses + 1
        print("Ah you missed!!! You need to improve your aim!!!\n")
        board[guess_row][guess_col] = 'X'
        print_board(board)


def game():
    """
    This function allows the player to a have a limited amount of guesses before 
    the game ends.
    """
    global bship_col
    global bship_row
    global game_active
    global guesses

    while guesses < 6:
        if game_active:
            user_guess()

            print()

            correct_guess()
        else:
            break
    if guesses <= 6 and game_active:
        print("Game over, No more guesses.\n")
        
    if not game_active:
        print(f"Congratulations, You guessed it in {guesses + 1} guesses\n")
        

def lets_go_again():
    """
    At the end of the game gives the player a option to play again
    or exit the game.
    """
    global game_active
    global guesses

    while True:
        replay = input("Would you like to play again commander 'Y' or 'N'\n").upper()
        clear()
        if replay == 'Y':
            game_active = True
            guesses = 0
            main()
        elif replay == 'N':
            game_active = False
            print("Enjoy your Retirement Commander\n")
            sys.exit()
        else:
            print("Invalid input. Please try again with only 'Y' & 'N'!!!\n")


def main():
    """
    Gives a replay function to the game.
    """
    global board

    new_board()

    lets_start()

    print_board(board)

    place_ship()

    game()

    lets_go_again()


if __name__ == "__main__":
    main()
