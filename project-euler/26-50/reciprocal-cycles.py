def repeating_decimal(n, d):
    x = n * 9
    z = x
    k = 1
    while z % d and k < d:
        z = z * 10 + x
        k += 1
    return k, z / d

max_d = 0
max_cycle = 0

for d in range(1, 1000):
    length, cycle = repeating_decimal(1, d)
    if length < d and length > max_cycle:
        max_d = d
        max_cycle = length

print max_d