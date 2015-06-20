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

n = 1
primes = [i for i in range(100) if is_prime(i)]

for prime in primes:
    if n * prime > 1000000:
        print n
        break
    n *= prime
