total = 0

for i in range(2, 1000001):
    if not (i % 2 == 0 or i % 3 == 0 or i % 5 == 0 or i % 7 == 0):
        total += i

print total