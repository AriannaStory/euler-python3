def smallest_multiple(ceiling: int):
    number = 1
    hit_limit = False

    while hit_limit == False:
        for i in range(1, (ceiling + 1)):
            if (number % i == 0):
                if (i == 20):
                    hit_limit = True
                    final_number = number
                    break
                i = i + 1
            else:
                number = number + 1
                break

smallest_multiple(5)