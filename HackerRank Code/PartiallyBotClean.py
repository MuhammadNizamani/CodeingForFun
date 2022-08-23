

def next_move(posx, posy, board):
    print(board)

if __name__ == "__main__": 
    pos = [int(i) for i in input().strip().split()] 
    # board = [[j for j in input().strip()] for i in range(5)] 
    board = [['b', 'd', '-', 'd', '-'],
             ['-', '-', 'd', '_', 'd'],
             ['-', 'd', '-', '-', '-'],
             ['-', '-', 'd', '-', '-'],
             ['-', 'd', '-', '-', 'd']]

    next_move(pos[0], pos[1], board)