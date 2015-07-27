def find_minimax(n, a, p, q):
    c = []
    for i in range(n - 1):
        if (a[i] + a[i + 1]) % 2 == 0:
            c.append((a[i] + a[i + 1]) / 2)
        else:
            c.append((a[i] + a[i + 1]) / 2)
            c.append((a[i] + a[i + 1]) / 2 + 1)
    c.append(p)
    c.append(q)
    c.sort()
    d, r = -1, 0
    for i in c:
        if i >= p and i <= q:
            l = 10 ** 9
            for j in a:
                l = min(l, abs(i - j))
            if l > d:
                d, r = l, i
    return r

n = int(raw_input())
a = sorted(list(map(int, raw_input().split())))
p, q = map(int, raw_input().split())
print find_minimax(n, a, p, q)
