import re

f = open('day6.txt', 'r')
grid = [[False for _ in range(1000)] for _ in range(1000)]

for line in f:
    instruction, x1, y1, x2, y2 = re.match('(.*) (\d+),(\d+) through (\d+),'
                                            '(\d+)', line.strip()).groups()
    x1, y1, x2, y2 = map(int, (x1, y1, x2, y2))
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            if instruction == 'toggle':
                grid[x][y] = not grid[x][y]
            elif instruction == 'turn on':
                grid[x][y] = True
            elif instruction == 'turn off':
                grid[x][y] = False

print(sum(1 if grid[x][y] else 0 for x in range(1000) for y in range(1000)))