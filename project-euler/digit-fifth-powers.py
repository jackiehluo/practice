n = []

for i in range(10, 1000000):
    num = str(i)
    total = 0
    for c in num:
        total += int(c) ** 5
    if i == total:
        n.append(i)

print n