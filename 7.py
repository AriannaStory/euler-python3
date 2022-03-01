def find_prime_number(index: int) -> int:
    i = 1
    prime_numbers = []

    while (len(prime_numbers) < index):
        if (is_prime(i)):
            prime_numbers.append(i)
        i = i + 1

    print(prime_numbers[(index - 1)])

def is_prime(number: int) -> bool:
    i = 1
    prime = False

    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                prime = False
                break
            i = i + 1
        else:
            prime = True

    return prime

find_prime_number(10001)