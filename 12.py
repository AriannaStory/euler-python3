def triangle_generator() -> int:
    triangle = 1
    number = 1

    while True:
        yield triangle
        number += 1
        triangle += number

def get_factors(number :int) -> list:
    divisor = 1
    limit = number
    factors = []

    while divisor <= limit:

        if (number % divisor == 0):
            factors.append(divisor)

            remainder = number // divisor

            if remainder != divisor:
                factors.append(remainder)

            limit = remainder - 1

        divisor += 1

    return factors

numbers = triangle_generator()
number = next(numbers)
factors = get_factors(number)

while len(factors) <= 500:
    number = next(numbers)
    factors = get_factors(number)

print(number)
