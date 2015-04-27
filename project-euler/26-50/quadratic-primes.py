from math import sqrt

def prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    else:
        for div in range(2, int(sqrt(n)) + 1):
            if n % div == 0:
                return False
        return True

max_primes = 0
product = 0

for i in range(-999, 1001):
    for j in range(-999, 1001):
        n = 0
        while True:
            s = n ** 2 + i * n + j
            if prime(s) == False:
                break
            if n > max_primes:
                max_primes = n
                product = i * j
            n += 1

print product