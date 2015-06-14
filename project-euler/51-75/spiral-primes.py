from math import sqrt

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    else:
        for div in range(2, int(sqrt(n)) + 1):
            if n % div == 0:
                return False
        return True

n = 2
last = 9
total = 3

while total / ((n - 1.0) * 4 + 1) > 0.1:
    n += 1
    for i in range(4):
        last += (n - 1) * 2
        if is_prime(last):
            total += 1

print 2 * n - 1
