import time

start_time = time.time()

def special_pythagorean_triplet(sum :int) -> dict:
    a = 0
    b = 0
    c = 0

    for a in range(1, sum):
        for b in range(1, sum):
            c = sum - a - b

            if ((pow(a, 2)) + (pow(b, 2)) == (pow(c, 2))):
                return (a * b * c)

print(special_pythagorean_triplet(1000))

end_time = time.time()

print('Execution Time: ', (end_time - start_time),'s', sep='')