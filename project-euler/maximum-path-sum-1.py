def max_sum(rows):
    for i in range(len(rows) - 2, -1, -1):
        for j in range(i + 1):
            rows[i][j] += max([rows[i + 1][j], rows[i + 1][j + 1]])
    return rows[0][0]

f = open('maximum-path-sum-1.txt', 'r')
rows = []

for line in f:
    rows.append([int(x) for x in line.split()])

print max_sum(rows)