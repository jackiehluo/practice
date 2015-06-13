n = 3
d = 2
count = 0

for i in range(1, 1000):
    n += 2 * d
    d = n - d
    if len(str(n)) > len(str(d)):
        count += 1

print count