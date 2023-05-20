def displayPathtoPrincess(n, grid):
    for idx, row in enumerate(grid):
        if 'p' in row:
            # print(idx, row)
            idp = idx

        # lst = list(row)

        # print(lst)

            if row[0] == 'p':
                s = 'l'
            else:
                s = 'r'
        # print(s)
        if 'm' in row:
        # print(idx, row)
            idm = idx
    if idm < idp:
        p = idp - idm
        if s == 'l':
            print(p*"DOWN\n", p*"LEFT\n", end="")
        else:
            print(p*"DOWN\n", p*"RIGHT\n", end="")
    if idm > idp:
        p = idm - idp
        if s == 'l':
            print(p*"UP\n", p*"LEFT\n", end="")
        else:
            print(p*"UP\n", p*"RIGHT\n", end="")



m = int(input())
grid = []
for i in range(0, m):
    grid.append(input().strip())

displayPathtoPrincess(m, grid)
