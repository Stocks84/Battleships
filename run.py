from random import randint

board = []

for _ in range(0, 8):
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

def random_column(board):
    """
    This gives a random number on the column which will essentially
    be our 'Hidden ship'. Regardless of the size of the board.
    """
    return randint(0, len(board) -1)
    
print_board(board)
