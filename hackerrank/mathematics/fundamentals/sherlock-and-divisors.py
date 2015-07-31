from math import sqrt

t = int(raw_input())
for _ in range(t):
    n = int(raw_input())
    factors = set(reduce(list.__add__, ([i, n / i]
            for i in range(1, int(sqrt(n)) + 1) if n % i == 0)))
    count = 0
    for f in factors:
        count += 1 if f % 2 == 0 else 0
    print count
