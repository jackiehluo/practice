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

circular_primes = set()

for i in range(2, 1000000):
    n = str(i)
    cp = True
    for j in range(len(n)):
        n = n[1:] + n[0]
        if not prime(int(n)):
            cp = False
            break
    if cp == True:
        circular_primes.add(i)

print len(circular_primes)