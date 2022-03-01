def even_fibonacci_numbers(start, limit: int):
    previous_number = start # 1
    next_number = start # 1
    sum = 0

    while previous_number < limit:
        operation = previous_number + next_number # Perform the operation

        next_number = previous_number
        previous_number = operation

        if (operation % 2 == 0): # Check if the next Fibonacci number is even, and...
            sum = sum + operation # ... if so, add it to our running total.

        # sum = sum + operation if operation % 2 == 0 else sum == sum

    print(sum)

even_fibonacci_numbers(1, 4000000)