from math import factorial

def binomial_coeff(n, k):
    return factorial(n) / (factorial(k) * factorial(n-k))

print( binomial_coeff(20 + 20, 20) )