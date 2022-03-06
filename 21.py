def sum_of_factors(number :int) -> int:
    total = []

    for i in range (1, number // 2 + 1):
        if not (number % i):
            total.append(i)
            i += 1

    return sum(total)

def sum_amicable_numbers(number :int) -> int:
    amicable_numbers = set()

    for i in range(1, 10000):
        x = sum_of_factors(i)
        y = sum_of_factors(x)

        if (i == y) and (x != y):
            amicable_numbers.add(x)

    return sum(amicable_numbers)

print(sum_amicable_numbers(10000))