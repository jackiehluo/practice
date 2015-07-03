def find_change(n, m, coins):
    combinations = {}
    for i in range(n + 1):
        combinations[i] = {}
    for j in range(1, m + 1):
        combinations[0][j] = 1
    for i in range(1, n + 1):
        combinations[i][0] = 0
        for j in range(1, m + 1):
            value = combinations[i][j - 1]
            if coins[j - 1] <= i:
                value += combinations[i - coins[j - 1]][j]
            combinations[i][j] = value
    return combinations[n][m]

n, m = map(int, raw_input().split())
coins = list(map(int, raw_input().split()))
print find_change(n, m, coins)