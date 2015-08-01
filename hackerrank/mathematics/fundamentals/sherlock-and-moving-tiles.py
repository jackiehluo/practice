from math import sqrt

l, s1, s2 = map(int, raw_input().split())
q = int(raw_input())
v = abs(s1 - s2) / sqrt(2)
for _ in range(q):
    print format((l - sqrt(int(raw_input()))) / v, '10.22f')
