def max_stock(n, prices):
    high = 0
    profit = 0
    for i in range(n - 1, -1, -1):
        if prices[i] >= high:
            high = prices[i]
        profit += high - prices[i]
    print profit

t = int(raw_input())

for case in range(t):
    n = int(raw_input())
    prices = [int(x) for x in raw_input().split()]
    max_stock(n, prices)
