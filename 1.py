def find_sum_multiples_3_5(limit: int):
    i = 1
    sum = 0
    while i < limit:
        print('Attempting to check',i,'%',limit)
        if (i % 3 == 0)  or (i % 5 == 0):
            sum += i
        i = i + 1
    print(sum)

find_sum_multiples_3_5(1000) # 233168