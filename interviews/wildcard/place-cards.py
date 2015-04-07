from math import factorial

f = open('problem1input.txt', 'r')
total = 0
grid = []

for line in f:
    empty = 0
    for c in line:
        if c == '*':
            empty += 1
    if empty >= 5:
        total += factorial(empty) / factorial(empty - 5)
    grid.append(list(line))

for col in range(len(line)):
    empty = 0
    for row in range(len(grid)):
        if grid[row][col] == '*':
            empty += 1
    if empty >= 5:
        total += factorial(empty) / factorial(empty - 5)

print total