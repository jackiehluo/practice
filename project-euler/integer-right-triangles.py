max_solutions = 0
number = 0

for i in range(4, 1001, 2):
    solutions = 0
    for j in range(2, i / 3 + 1):
        if i * (i - 2 * j) % (2 * (i - j)) == 0:
            solutions += 1
    if solutions > max_solutions:
        max_solutions = solutions
        number = i

print number