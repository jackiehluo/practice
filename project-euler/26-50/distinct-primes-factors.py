from math import sqrt

def prime_factorize(n):
    factors = []
    number = abs(n)
    while number > 1:
        factor = get_next_prime(number)
        factors.append(factor)
        number /= factor
    if n < -1:
        factors[0] = -factors[0]
    return factors

def get_next_prime(n):
    if n % 2 == 0:
        return 2
    for x in range(3, int(sqrt(n) + 1), 2):
        if n % x == 0:
            return x
    return n

i = 647
j = 648
k = 649
l = 650

while True:
    if (len(set(prime_factorize(i))) == 4 and
        len(set(prime_factorize(j))) == 4 and
        len(set(prime_factorize(k))) == 4 and
        len(set(prime_factorize(l))) == 4):
        print i
        break
    i += 1
    j += 1
    k += 1
    l += 1