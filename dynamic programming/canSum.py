def canSum(tragetSum, numbers, memo={}):
    if tragetSum in memo:
        return memo[tragetSum]
    if tragetSum == 0:
        return True
    if tragetSum < 0:
        return False
    for num in numbers:
        remainder = tragetSum - num
        if canSum(remainder, numbers, memo) == True:
            memo[tragetSum] = True
            return True
    memo[tragetSum] = False
    return False


print(canSum(900, [3,7, 14]))
print(canSum(8, [2, 3, 5]))
