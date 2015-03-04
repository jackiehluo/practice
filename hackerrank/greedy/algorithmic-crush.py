n, m = (int(x) for x in raw_input().split())
d = dict.fromkeys(range(1, n + 1), 0)

for op in range(m):
    a, b, k = (int(y) for y in raw_input().split())
    for i in range(a, b + 1):
        d[i] += k

print d[max(d, key = d.get)]
