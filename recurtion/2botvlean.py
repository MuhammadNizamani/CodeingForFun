import math

# Update cost that bot need to arrive the dirty


def update_position(posr, posc, dirties):
    nearest_dirt = []
    for i in range(len(dirties)):
        # Euclidean distance
        result = math.sqrt(
            ((dirties[i][0] - posr) ** 2) + ((dirties[i][1] - posc) ** 2))
        nearest_dirt.append(result)
    a = [x for (y, x) in sorted(zip(nearest_dirt, dirties))]
    print(a)
    return a

# Set the bot in your new position


def next_move(posr, posc, board):
    dirties = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'd':
                dirties.append([i, j])

    next_dirt = update_position(posr, posc, dirties)
    if next_dirt[0][1] < posc:
        print('LEFT')
    elif next_dirt[0][1] > posc:
        print('RIGHT')
    elif next_dirt[0][0] < posr:
        print('UP')
    elif next_dirt[0][0] > posr:
        print('DOWN')
    else:
        print('CLEAN')


# Tail starts here

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
