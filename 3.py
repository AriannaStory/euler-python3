def largest_prime_factor(number: int):
    i = 1
    factors = []
    composite_factors = []

    # First, let's get all of the number's factors...
    while i < (number / 2):
        if (number % i == 0):
            factors.append(i)
            i = i + 1
        else:
            i = i + 1
    print(factors)

    for factor in factors:
        if factor > 1: # Given that "1" cannot be a prime number
            for i in range(1, (factor + 1)):
                result = factor % i
                print(factor, '%', i, '=', result)
                if ((result == 0) and (i != 1) and (i != factor)):
                    composite_factors.append(factor)
                    print(factor, 'is not a prime number.')
                    break

    prime_factors = set(factors) - set(composite_factors)

    print(max(prime_factors))

# largest_prime_factor(100000)
largest_prime_factor(600851475143)