n, p, x = map(int, raw_input().split())
a = list(map(int, raw_input().split()))
maximum = 0

for i in range(n):
    if a[i] * p > maximum:
        applicant = i + 1
        maximum = a[i] * p
    p -= x

print applicant