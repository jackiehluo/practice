def diff(a, b):
    total = 0.0
    for i in range(len(a)):
        total += abs(a[i] - b[i])
    return total

def minimum_index(mins):
    m, ind = mins[0], 0
    for i in range(len(mins)):
        if mins[i] < m:
            m, ind = mins[i], i
    return ind

n = int(raw_input())
original, approximate = [], []
for i in range(n):
    line = list(map(float, raw_input().split(',')))
    original.append(line)
for i in range(n):
    line = list(map(float, raw_input().split(',')))
    approximate.append(line)
for i in range(n):
    mins = []
    for j in range(n):
        mins.append(diff(original[i], approximate[j]))
    print str(i) + "," + str(minimum_index(mins))