def max_couples(m, f):
    m.sort()
    f.sort()
    hotness = 0
    for i in range(len(m)):
        hotness += m[i] * f[i]
    return hotness

t = int(raw_input())

for case in range(t):
    length = int(raw_input())
    m = [int(x) for x in raw_input().split()]
    f = [int(y) for y in raw_input().split()]
    answer = max_couples(m, f)
    print answer
