from math import floor

def compare(j, k, base, comp):
    words = 0
    for p in base:
        for q in comp:
            ind = 0
            match = 0.0
            while p[ind] == q[ind]:
                match += 1
                ind += 1
            prefix = int((match / len(q)) * 100)
            if prefix >= j:
                words += 1
    if floor(words / len(base) * 100) >= k:
        return int(floor(words / len(base) * 100))
    else:
        return 0

j = int(raw_input())
k = int(raw_input())
n = int(raw_input())
m = int(raw_input())

base = []
comp = []

for _ in range(n):
    base.append(raw_input())
for _ in range(m):
    comp.append(raw_input())

print compare(j, k, base, comp)
