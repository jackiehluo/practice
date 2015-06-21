def check_columns(n, grid):
    if n > 2:
        for c in range(n):
            for r in range(n - 1):
                if grid[r][c] > grid[r + 1][c]:
                    return False
        return True
    elif n == 2:
        if grid[0][0] > grid[1][0] or grid[0][1] > grid[1][1]:
            return False
        return True
    else:
        return True

t = int(raw_input())

for case in range(t):
    grid = []
    n = int(raw_input())
    for i in range(n):
        line = sorted(list(raw_input()))
        grid.append(line)
    answer = check_columns(n, grid)
    if answer == True:
        print "YES"
    else:
        print "NO"
