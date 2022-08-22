def nextMove(n, r, c, grid):
    for idx, row in enumerate(grid):
        if 'p' in row:
            # print(idx, row)
            if idx < r:
                r = r-1

                return "UP"
            elif idx > r:
                r = r+1
                return "DOWN"
            elif idx == r:
                for i in range(0, len(row)):
                    if row[i] == 'p':
                        if i < c:
                            c = c-1
                            return "LEFT"
                        else:
                            c = c+1
                            return "RIGHT"

            # lst = list(row)

            # print(lst)

    return ""


n = int(input())
r, c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(grid)
print(nextMove(n, r, c, grid))
