from random import randint

board = []

for x in range(0, 8):
    board.append(['O'] * 8)

# print(board)

def print_board(board):
    """
    This is for the aesthetics of the game.
    Making nice rows for the user.
    """
    for row in board:
        print(' '.join(row))

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

guess_row = int(input("Guess Row: "))
guess_col = int(input("Guess Col: "))

print(bship_row)
print(bship_col)

# print_board(board)
