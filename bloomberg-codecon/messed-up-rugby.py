n = int(raw_input())

for i in range(n / 7 + 1):
    for j in range(n / 3 + 1):
        for k in range(n / 2 + 1):
            if i * 7 + j * 3 + k * 2 == n:
                print i, j, k
