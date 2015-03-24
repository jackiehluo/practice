def count(cards):
    c = sorted(cards)
    ways = 1
    for i in range(len(cards), 0, -1):
        ways *= i - c[i - 1]
        ways %= 1000000007
    return ways

t = int(raw_input())

for case in range(t):
    n = int(raw_input())
    cards = [int(x) for x in raw_input().split()]
    print count(cards)