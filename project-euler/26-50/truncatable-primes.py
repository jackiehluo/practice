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

truncatable_primes = []

for i in range(10, 1000000):
    if prime(i):
        m = str(i)
        n = str(i)
        p = True
        for j in range(len(m) - 1):
            n = n[1:]
            m = m[:-1]
            if not prime(int(m)) or not prime(int(n)):
                p = False
                break
        if p == True:
            truncatable_primes.append(i)

print sum(truncatable_primes)