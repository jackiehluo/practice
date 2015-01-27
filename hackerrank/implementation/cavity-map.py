def find_cavities(cavity_map):
    for i in range(1, size - 1):
        for j in range(1, size - 1):
            if (cavity_map[i][j] > cavity_map[i - 1][j]) and (cavity_map[i][j] > cavity_map[i][j - 1]) and (cavity_map[i][j] > cavity_map[i + 1][j]) and (cavity_map[i][j] > cavity_map[i][j + 1]):
                cavity_map[i][j] = "X"
    return cavity_map
    
size = int(raw_input())
cavity_map = []

for row in range(size):
    line = raw_input()
    cavity_map.append(map(int, line))

find_cavities(cavity_map)

for k in range(size):
    print ''.join(map(str, cavity_map[k]))