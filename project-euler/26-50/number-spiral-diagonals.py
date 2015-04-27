def diagonal_sum(n):
    count = 1
    last = 1
    total = last
    while count < 2 * n - 1:
        i = int(count * 0.5 + 1.5)
        for p in range(4):
            last += i
            total += last
            count += 1
    return total

print diagonal_sum(1001)