def sundays_in_range(start: int, end: int):

    sundays = 0
    day = 1

    days_in_month = [
        31,
        28,
        31,
        30,
        31,
        30,
        31,
        31,
        30,
        31,
        30,
        31
    ]

    for year in range(start, end):

        for month in range(0, len(days_in_month)):

            if ((year % 4 == 0) and (month == 2)): # Add an extra day for leap years
                if ((year % 100) and (year % 400)):
                    day += 1
            if ((day % 7 == 0) and (year != 1900)): # Skip counting for the first year, since we're looking for 1901 - 2000; if day % 7 == 0, it's a Sunday
                sundays += 1

            day += days_in_month[month]

    print(sundays)


sundays_in_range(1900, 2001)