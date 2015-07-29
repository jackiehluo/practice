def cut(l, b):
    for i in range(1, min(l, b) + 1):
        if l % i == 0 and b % i == 0:
            s = (l / i) * (b / i)
    return s

t = int(raw_input())

for case in range(t):
    l, b = (int(x) for x in raw_input().split())
    print cut(l, b)