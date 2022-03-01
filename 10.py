import sympy

def get_primes(limit :int) -> list:
    primes = list(sympy.primerange(0,limit))
    return primes

def sum_list(list: list) -> int:
    sum = 0

    for val in list:
        print(sum, '+', val, '=',(sum + val))
        sum = sum + val

    return sum

print(sum_list(get_primes(2000000)))