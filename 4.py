def largest_palindrome_product(length :int):
    highest_number = ''
    palindromes = []

    while len(highest_number) < length:
        highest_number = highest_number + '9'

    highest_number = int(highest_number)

    for i in range(1, (highest_number + 1)):
        for s in range (1, (highest_number + 1)):
            solution = i * s
            solution = str(solution)
            if (solution == solution[::-1]):
                palindromes.append(int(solution))

    print(sorted(palindromes)[-1])

largest_palindrome_product(3)