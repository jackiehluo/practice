def count_candies(ratings):
    n = len(ratings)
    total = 0
    left, right = [1] * n, [1] * n
    for i in range(n - 2, -1, -1):
        if ratings[i + 1] < ratings[i]:
            right[i] = right[i + 1] + 1
    for i in range(1, n):
        if ratings[i - 1] < ratings[i]:
            left[i] = left[i - 1] + 1
    for i in range(n):
        total += max(right[i], left[i])
    return total

ratings = []
for _ in range(int(raw_input())):
    ratings.append(int(raw_input()))
print count_candies(ratings)