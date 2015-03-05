def trailing_zeroes(n):
    count = 0
    power = 0
    while n / 5 ** power >= 1:
        power += 1
        count += n / 5 ** power
    return count

t = int(raw_input())

for case in range(t):
    n = int(raw_input())
    zeroes = trailing_zeroes(n)
    print zeroes
