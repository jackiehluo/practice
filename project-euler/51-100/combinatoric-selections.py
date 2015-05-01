from operator import mul

def ncr(n, r):
    r = min(r, n - r)
    if r == 0:
        return 1
    num = reduce(mul, xrange(n, n - r, -1))
    denom = reduce(mul, xrange(1, r + 1))
    return num / denom

count = 0

for i in range(1, 101):
    for j in range(1, i):
        if ncr(i, j) > 1000000:
            count += 1

print count