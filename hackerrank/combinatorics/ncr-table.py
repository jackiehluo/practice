from operator import mul

def ncr(n, r):
    r = min(r, n - r)
    if r == 0:
        return 1
    num = reduce(mul, xrange(n, n - r, -1))
    denom = reduce(mul, xrange(1, r + 1))
    return num / denom

t = int(raw_input())

for case in range(t):
    n = int(raw_input())
    table = []
    for i in range(n + 1):
        table.append(ncr(n, i) % 1000000000)
    print " ".join(map(str, table))
