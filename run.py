from random import randint

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



bship_row = random_row(board)
bship_col = random_col(board)
# Delete these prints after testing and undo comment down below
print(bship_row)
print(bship_col)
guess_row = int(input("Guess Row: "))
guess_col = int(input("Guess Col: "))

# print(bship_row)
# print(bship_col)


def correct_guess():
    """
    When player gets a correct guess a message will appear.
    """
    if guess_row == bship_row and guess_col == bship_col:
        print("BOOM!!! That was a Great hit!\n")
    # else:
    #     print("Ah you missed!!! You need to improve your aim!!!\n")
    #     board[guess_row][guess_col] = 'X'
    #     print_board(board)


correct_guess()

# Might need to be before correct guess function
def land_guess():
    """
    When player guesses out of range of the board a message will appear.
    """
    if guess_row not in range(8) or guess_col not in range(8):
        print("Oh no, you have hit DRY LAND!!! Please try again!!")
        print("Anywhere between 1 & 8 \n")

land_guess()
