from math import sqrt

k, n = map(int, raw_input().split())
radii = list(map(int, raw_input().split()))
radii.append(0)
total = 0
for i in range(n):
    x, y = map(int, raw_input().split())
    r = sqrt(x ** 2 + y ** 2)
    for i in range(1, k + 1):
        if r == 0:
            total += k
            break
        elif r > radii[i] and r <= radii[i - 1]:
            total += i
            break
print total