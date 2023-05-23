function = lambda x: 1 / (x**2)

def srule(x, step):
    sum = function(1 + step) + function(1 + x * step)
    
    # Using round() which returns a floating point number
    n = round((x - 1) / step)
    i = x + step
    
    # for loop that has the range from 1 to n - 1
    i = 1
    while i<n-1:
        sum = sum + ((2 if i % 2 == 0 else 4)) * function(1 + i * step)
        i = i + step
    
    # retun the sum multiplied with the stepsized divided with 3
    return sum * (step / 3)
