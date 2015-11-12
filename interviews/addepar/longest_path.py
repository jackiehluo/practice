def longest_path(grid):
    coordinates = {}
    for r in range(len(grid)):
        for c in range(len(grid)):
            n = grid[r][c]
            coordinates[n] = (r, c)
    cur_length, max_length = 1, 1
    for key in range(1, len(grid) ** 2):
        cur_r, cur_c = coordinates[key]
        next_r, next_c = coordinates[key + 1]
        diff = abs(cur_r - next_r) + abs(cur_c - next_c)
        if diff == 1:
            cur_length += 1
            max_length = max(max_length, cur_length)
        else:
            cur_length = 1
    return max_length