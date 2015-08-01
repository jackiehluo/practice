n, k = map(int, raw_input().split())
ids = set(map(int, raw_input().split()))

for i in xrange(1, n + 1):
    if i + 1 not in ids and i - 1 not in ids:
        ids.add(i)

print len(ids)