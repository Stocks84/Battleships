board = []

for _ in range(0, 10):
    board.append(['0'] * 10)

# print(board)

def print_board(board):
    """
    This is for the asthetics of the game.
    Making nice rows for the user.
    """
    for row in board:
        print(row)

print_board(board)
