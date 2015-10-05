class Solution(object):
    def minPathSum(self, grid):
        if len(grid) == 0 or len(grid[0]) == 0: return 0
        for r in range(0, len(grid)):
            for c in range(0, len(grid[r])):
                if r > 0 and c > 0:
                    grid[r][c] += min(grid[r - 1][c], grid[r][c - 1])
                elif r > 0:
                    grid[r][c] += grid[r - 1][c]
                elif c > 0:
                    grid[r][c] += grid[r][c - 1]
        return grid[len(grid) - 1][len(grid[0]) - 1]