def is_lychrel(n):
    for i in range(50):
        n += int(str(n)[::-1])
        if str(n) == str(n)[::-1]:
            return False
    return True

count = 0

for i in range(1, 10000):
    if is_lychrel(i):
        count += 1

print count