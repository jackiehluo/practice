from collections import Counter
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

n = 1

while True:
	triangle = n * (n + 1) / 2
	factors = prime_factorize(triangle)
	counts = Counter(factors)
	divisors = 1
	for k, v in counts.iteritems():
		divisors *= v + 1
	if divisors >= 500:
		print triangle
		break
	n += 1