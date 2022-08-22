def next_move(posr, posc, board):
    for i in range(0, 5):
        if board[posr][i] == 'd':
            if posc < i:
                a = posc
                b = i
            else:
                a = i
                b = posc
            for j in range(a, b+1):
                if posc < i:
                    posc += 1
                    print("RIGHT")
                elif posc > i:
                    posc -= 1
                    print("LEFT")
                elif posc == i:
                    print("CLEAN")
    print("DOWN")
    posr += 1
    for i in range(0, 5):
        if board[posr][i] == 'd':
            if posc < i:
                a = posc
                b = i
            else:
                a = i
                b = posc
            for j in range(a, b+1):
                if posc < i:
                    posc += 1
                    print("RIGHT")
                elif posc > i:
                    posc -= 1
                    print("LEFT")
                elif posc == i:
                    print("CLEAN")
    print("DOWN")
    posr += 1
    for i in range(0, 5):
        if board[posr][i] == 'd':
            if posc < i:
                a = posc
                b = i
            else:
                a = i
                b = posc
            for j in range(a, b+1):
                if posc < i:
                    posc += 1
                    print("RIGHT")
                elif posc > i:
                    posc -= 1
                    print("LEFT")
                elif posc == i:
                    print("CLEAN")
    print("DOWN")
    posr += 1
    for i in range(0, 5):
        if board[posr][i] == 'd':
            if posc < i:
                a = posc
                b = i
            else:
                a = i
                b = posc
            for j in range(a, b+1):
                if posc < i:
                    posc += 1
                    print("RIGHT")
                elif posc > i:
                    posc -= 1
                    print("LEFT")
                elif posc == i:
                    print("CLEAN")
    print("DOWN")
    posr += 1
    for i in range(0, 5):
        if board[posr][i] == 'd':
            if posc < i:
                a = posc
                b = i
            else:
                a = i
                b = posc
            for j in range(a, b+1):
                if posc < i:
                    posc += 1
                    print("RIGHT")
                elif posc > i:
                    posc -= 1
                    print("LEFT")
                elif posc == i:
                    print("CLEAN")


if __name__ == "__main__":
    a = 0
    b = 0
    n = 5
    board = [['b', 'd', '-', 'd', '-'],
             ['-', '-', 'd', '_', 'd'],
             ['-', 'd', '-', '-', '-'],
             ['-', '-', 'd', '-', '-'],
             ['-', 'd', '-', '-', 'd']]

next_move(a, b, board)
