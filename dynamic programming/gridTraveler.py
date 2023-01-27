def gridTraveler(m, n):
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    return gridTraveler(m-1, n) + gridTraveler(m, n-1)


# it's not working for 18 by 18 grid becuase it's to slow
print(gridTraveler(18, 18))
