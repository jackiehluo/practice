def blacklist(r):
    total = 0
    for l in r:
        total += min(l)
    return total

n, k = (int(x) for x in raw_input().split())
r = [[] for g in xrange(n)]
for m in range(k):
    ir = [int(y) for y in raw_input().split()]
    for p in range(n):
        r[p].append(ir[p])
print blacklist(r)
