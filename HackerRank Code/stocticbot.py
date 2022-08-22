#!/bin/python3

def nextMove(posr, posc, board):
    c=0
    r =0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 'd':
                c= j
                r = i

    if c < posc:
        print("LEFT")
    elif c> posc:
        print("RIGHT")
    elif r <posr:
        print("UP")
    elif r> posr:
        print("DOWN")
    else:
        print("CLEAN")


if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    nextMove(pos[0], pos[1], board)
