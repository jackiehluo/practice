from math import factorial

f = open('problem1input.txt', 'r')
total = 0
grid = []

for line in f:
    empty = 0
    r = []
    for c in line:
        r.append(c)
        if c == '*':
            empty += 1
    if empty >= 5:
        total += factorial(empty) / factorial(empty - 5)
    grid.append(r)

for col in range(50):
    empty = 0
    for row in range(len(grid)):
        if grid[row][col] == '*':
            empty += 1
    if empty >= 5:
        total += factorial(empty) / factorial(empty - 5)

print total