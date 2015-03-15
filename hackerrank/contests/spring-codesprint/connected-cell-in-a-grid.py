lls():
    max_cells = 0
    visits = [[0 for col in range(n)] for row in range(m)]
    for r in range(m):
        for c in range(n):
            max_cells = max(connected_cells(r, c, visits), max_cells)
    return max_cells
            
def connected_cells(r, c, visits):
    size = 0
    if r < m and r >= 0 and c < n and c >= 0:
        if grid[r][c] == 1 and visits[r][c] == 0:
            size += grid[r][c]
            visits[r][c] = 1
            size += connected_cells(r, c + 1, visits)
            size += connected_cells(r, c - 1, visits)
            size += connected_cells(r + 1, c, visits)
            size += connected_cells(r - 1, c, visits)
            size += connected_cells(r + 1, c + 1, visits)
            size += connected_cells(r - 1, c + 1, visits)
            size += connected_cells(r + 1, c - 1, visits)
            size += connected_cells(r - 1, c - 1, visits)
    return size

m = int(raw_input())
n = int(raw_input())
grid = []

for i in range(m):
    line = [int(x) for x in raw_input().split()]
    grid.append(line)

print max_cells()
