from math import sqrt

def factor_sum(n):
    return sum(set(reduce(list.__add__,
                ([i, n // i] for i in range(1, int(sqrt(n)) + 1) if n % i == 0)))) - n

amicables = set()

for i in xrange(2, 10001):
    sum_a = factor_sum(i)
    if i != sum_a and factor_sum(sum_a) == i:
        amicables.add(i)
        amicables.add(sum_a)

print sum(amicables)