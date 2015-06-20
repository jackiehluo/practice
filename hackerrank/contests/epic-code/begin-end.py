from collections import Counter

n = int(raw_input())
s = raw_input()
total = 0

for v in Counter(s).values():
    total += v * (v + 1) / 2

print total