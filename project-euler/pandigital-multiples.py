pan = "123456789"
max_n = 0

for i in range(9000, 100000):
    m = 1
    n = ""
    while True:
        n += str(i * m)
        m += 1
        if len(n) >= 9:
            break
    if "".join(sorted(n)) == pan and int(n) > max_n:
        max_n = int(n)

print max_n