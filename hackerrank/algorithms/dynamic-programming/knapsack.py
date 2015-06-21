def knapsack(numbers, total):
    k = [0]
    for i in range(1, total + 1):
        price = [k[i - v] + v for v in numbers if i >= v]
        k.append(max(price) if price else k[-1])
    return k[-1]

t = int(raw_input())

for _ in range(t):
    n, k = (int(x) for x in raw_input().split())
    numbers = [int(y) for y in raw_input().split()]
    print knapsack(numbers, k)