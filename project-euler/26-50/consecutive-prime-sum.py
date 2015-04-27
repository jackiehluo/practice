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

primes = [int(i) for i in range(1, 1000000) if prime(i)]
sums = [0] * (len(primes) + 1)

for j in range(len(primes)):
    sums[j + 1] = sums[j] + primes[j]

n = 0

for k in range(n, len(sums)):
    for l in range(k - n - 1, -1, -1):
        if sums[k] - sums[l] > 1000000:
            break
        if sums[k] - sums[l] in primes:
            n = k - l
            answer = sums[k] - sums[l]

print answer