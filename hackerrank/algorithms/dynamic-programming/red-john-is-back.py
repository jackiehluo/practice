from math import sqrt

wall = [0] * 41
wall[0:4] = [1] * 4
for i in range(4, 41):
    wall[i] = wall[i - 1] + wall[i - 4]
puzzle = [True] * 220000
puzzle[0], puzzle[1] = False, False
for i in range(2, int(sqrt(220000))):
    if puzzle[i]:
        for j in range(i * i, 220000, i):
            puzzle[j] = 0

for _ in range(int(raw_input())):
    total = 0
    for i in range(wall[int(raw_input())] + 1):
        if puzzle[i]:
            total += 1
    print total
