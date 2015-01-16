def find_min(n, k, candies):
    min = candies[n - 1]
    for i in range(n - k - 1):
        if (candies[i + k - 1] - candies[i]) < min:
            min = candies[i + k - 1] - candies[i]
    return min

n = input()
k = input()
candies = [input() for _ in range(0, n)]
candies.sort()
min_diff = find_min(n, k, candies)
print min_diff