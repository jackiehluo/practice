from collections import Counter

def gigaball(a, b, c):
    combinations = []
    for i in a:
        for j in b:
            for k in c:
                combinations.append(i + j + k)
    counts = Counter(combinations)
    return counts.most_common()[0][0]

a = []
b = []
c = []
l, m, n = (int(x) for x in raw_input().split())

for _ in range(l):
    a.append(int(raw_input()))
for _ in range(m):
    b.append(int(raw_input()))
for _ in range(n):
    c.append(int(raw_input()))
print gigaball(a, b, c)
