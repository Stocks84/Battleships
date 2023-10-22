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

print_board(board)
