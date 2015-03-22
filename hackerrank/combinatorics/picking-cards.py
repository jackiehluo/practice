def count(cards, m):
    count = 0
    for value in cards:
        if value <= m:
            count += 1
    return count

t = int(raw_input())

for case in range(t):
    n = int(raw_input())
    cards = [int(x) for x in raw_input().split()]
    total = 1;
    for i in range(len(cards)):
        ways = max(0, count(cards, i) - i)
        total = (total * ways) % 1000000007
    print total