from math import factorial

def get_factorial_sum(number :int) -> int:
    list = []
    sum = 0
    list = [int(a) for a in str(factorial(number))]

    for num in list:
        sum += num
    print(sum)

get_factorial_sum(100)