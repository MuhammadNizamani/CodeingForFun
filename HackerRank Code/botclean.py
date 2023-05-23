
# Head ends here

def next_move(posr, posc, board):
    print(board[0])

# Tail starts here


if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    # print(pos)
    board = [[j for j in input().strip()] for i in range(5)]
    # print(board)
    next_move(pos[0], pos[1], board)
