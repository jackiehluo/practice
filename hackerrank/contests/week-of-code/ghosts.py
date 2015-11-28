from fractions import gcd

a, b, c, d = map(int, raw_input().split())
count = 0
for i in range(1, a + 1):
    for j in range(1, b + 1):
        for k in range(1, c + 1):
            for l in range(1, d + 1):
                if (abs(i - j) % 3 == 0 and (j + k) % 5 == 0 and
                   (i * k) % 4 == 0 and gcd(i, l) == 1):
                    count += 1
print count