def fib (num):
    if num ==0 or num ==1:
        return num

    return fib(num-1) +fib(num-2)



print(fib(20))