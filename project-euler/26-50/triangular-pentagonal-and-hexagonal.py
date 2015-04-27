from math import sqrt

def pentagonal(n):
    p = (sqrt(1 + 24 * n) + 1.0) / 6.0
    return p == int(p)

i = 143

while True:
    i += 1
    h = i * (2 * i - 1)
    if pentagonal(h):
        print h
        break