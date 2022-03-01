def sum_of_squares(number: int) -> int:
    i = 1;
    sum = 0;

    while i < (number + 1):
        sum = sum + (i ** 2)
        i = i + 1

    return sum

def square_of_sums(number: int) -> int:
    i = 1;
    sum = 0;

    while i < (number + 1):
        sum = sum + i
        i = i + 1

    sum = sum ** 2

    return sum

print(square_of_sums(100) - sum_of_squares(100))