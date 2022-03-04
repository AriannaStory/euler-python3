def collatz_sequence(n):
    chain = []
    result = n
    chain.append(int(result))
    while result != 1:
        if (result % 2 == 0): #even
            result = (result / 2)
            chain.append(int(result))
        else:
            result = (3 * result) + 1
            chain.append(int(result))

    return len(chain)

high_score = 0
high_number = 0

for num in range(1, 1000000):
    result = collatz_sequence(num)
    print(num, result)

    if (result > high_score):
        high_score = result
        high_number = num
        print('New high score by', num,'(',result, ')')

print(high_number, high_score)