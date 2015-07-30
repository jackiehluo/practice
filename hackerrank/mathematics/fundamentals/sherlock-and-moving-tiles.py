from math import sqrt

l, s1, s2 = map(int, raw_input().split())
q = int(raw_input())
for _ in range(q):
    print 2 * (l - sqrt(int(raw_input()))) / abs(s1 - s2) / sqrt(2)
