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

def goldbach(n):
    s = sqrt(n / 2.0)
    return s == int(s)

i = 1
not_found = True
primes = [int(x) for x in range(2, 10000) if prime(x)]

while not_found:
    i += 2
    if not prime(i):
        j = 0
        not_found = False
        while i >= primes[j]:
            if goldbach(i - primes[j]):
                not_found = True
                break
            j += 1

print i