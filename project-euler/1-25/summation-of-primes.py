from math import sqrt

x = 2000000
primes = []
for n in xrange(2, x + 1):
    for p in primes:
        if n % p == 0:
            break
        if n < p * p:
            primes.append(n)
            break
    else:
        primes.append(n)
print sum(primes)