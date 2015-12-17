from collections import defaultdict

f = open('day3.txt', 'r')
directions = {
                '^': (0, 1),
                'v': (0, -1),
                '>': (1, 0),
                '<': (-1, 0)
            }
grid = defaultdict(int, [((0, 0), 1)])
cur = [0, 0]

while True:
    pointer = f.read(1)
    try:
        cur[0] += directions[pointer][0]
        cur[1] += directions[pointer][1]
        key = tuple(cur)
        grid[key] += 1
    except:
        break

count = 0
for k, v in grid.items():
    if v > 0:
        count += 1

print count