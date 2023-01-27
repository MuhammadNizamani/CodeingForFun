def gridTraveler(m, n, memo={}):
    key = str(m) + "," + str(n)
    if key in memo:
        return memo[key]
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    memo[key] = gridTraveler(m-1, n, memo) + gridTraveler(m, n-1, memo)
    return memo[key]


# now this code run fast now it time complex reduce from expontent to polynolial
print(gridTraveler(18, 18))
