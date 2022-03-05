# Technically, the solution to "Find the sum of the digits in the number 100!" should be 1, but I digress...

from math import factorial

def get_factorial_sum(number :int) -> int:
    list = []
    sum = 0
    list = [int(a) for a in str(factorial(number))]

    for num in list:
        sum += num
    print(sum)

get_factorial_sum(100)