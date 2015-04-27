sundays = 0
days_in_month = 1
days = 1

for i in range(1900, 2001):
    for j in range(1, 13):
        if j == 4 or j == 6 or j == 9 or j == 11:
            days_in_month = 30
        elif j == 2:
            if (j % 100 == 0 and j % 400 == 0) or (j % 100 != 0 and j % 4 == 0):
                days_in_month = 29
            else:
                days_in_month = 28
        else:
            days_in_month = 31
        if i > 1900:
            if days % 7 == 0:
                sundays += 1
        days += days_in_month

print sundays
