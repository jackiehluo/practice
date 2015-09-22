def num_paths(N, M):
    grid = [[1] * M] * N
    for i in range(1, N):
        for j in range(1, M):
            grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
    return grid[N - 1][M - 1]