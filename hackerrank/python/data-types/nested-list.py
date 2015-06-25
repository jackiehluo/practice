n = int(raw_input())
grades = []

for _ in range(n):
    grades.append([raw_input(), float(raw_input())])

second_lowest = sorted(set([mark for name, mark in grades]))[1]

print '\n'.join(sorted([name for name, mark in grades if mark == second_lowest]))
