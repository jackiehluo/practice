from math import sqrt

def pentagonal(n):
    p = (sqrt(1 + 24 * n) + 1.0) / 6.0
    return p == int(p)

not_found = True
i = 0

while not_found:
    i += 1
    n = i * (3 * i - 1) / 2
    for j in range(i, 0, -1):
        m = j * (3 * j - 1) / 2
        if pentagonal(n - m) and pentagonal(n + m):
            print n - m
            not_found = False
            break