def update_list(n, m, d):
    d.sort()
    r, t = 0, 0
    for op in d:
        if op[1] == -1:
            t += op[2]
        else:
            t -= op[2]
        if t > r:
            r = t
    return r

n, m = map(int, raw_input().split())
d = []
for i in range(m):
    a, b, k = map(int, raw_input().split())
    d.append([a, -1, k])
    d.append([b, 1, k])
print update_list(n, m, d)