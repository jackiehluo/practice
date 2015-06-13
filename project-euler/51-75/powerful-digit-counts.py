from math import ceil

total = 0
lower = 0
n = 1

while lower < 10:
    lower = int(ceil(10 ** ((n - 1.0) / n)))
    total += 10 - lower
    n += 1

print total