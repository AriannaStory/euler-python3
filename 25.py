fibonacci = [0, 1]

i = 2

while True:
    new = fibonacci[i - 1] + fibonacci[i - 2]
    fibonacci.append(new)

    if new > pow(10,999):
        print(i)
        break

    i += 1