t = int(raw_input())
matrix = [[0 for x in range(2001)] for x in range(2001)]
matrix[1][0] = matrix[1][1] = 1
for i in range(2, 2001):
    matrix[i][0] = matrix[i][i] = 1
    for j in range(1, i):
        matrix[i][j] = (matrix[i - 1][j - 1] + matrix[i - 1][j]) % 1000000000
for _ in range(t):
    n = int(raw_input())
    k = int(raw_input())
    print matrix[n + k - 1][n - 1]
