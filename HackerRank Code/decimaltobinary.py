def decimalToBinary(num, result):
     
    if num ==0:
        return result

    result = str(num%2) + result
    return decimalToBinary(num//2, result)


a = 15
print(decimalToBinary(a, ""))