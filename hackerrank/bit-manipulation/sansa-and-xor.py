def xor(n, numbers):
    xor = 0
    for i, el in enumerate(numbers):
        if (i + 1) * (n - i) % 2 == 1:
            xor ^= el
    print xor

t = int(raw_input())

for case in range(t):
    n = int(raw_input())
    numbers = [int(x) for x in raw_input().split()]
    xor(n, numbers)
