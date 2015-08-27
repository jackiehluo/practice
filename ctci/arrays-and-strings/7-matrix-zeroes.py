import sys

def find_zeroes(grid):
    rows = set()
    columns = set()
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0:
                rows.add(i)
                columns.add(j)
    return rows, columns

def nullify_rows(grid, rows):
    for i in range(len(grid)):
        if i in rows:
            for j in range(len(grid[i])):
                grid[i][j] = 0
    return grid

def nullify_columns(grid, columns):
    for i in range(len(grid[0])):
        if i in columns:
            for j in range(len(grid)):
                grid[j][i] = 0
    return grid

m = int(sys.stdin.readline())
n = int(sys.stdin.readline())
grid = []

for _ in range(n):
    line = [int(x) for x in sys.stdin.readline().split()]
    grid.append(line)

rows, columns = find_zeroes(grid)
grid = nullify_rows(grid, rows)
grid = nullify_columns(grid, columns)

for i in range(len(grid)):
    print " ".join(map(str, grid[i]))