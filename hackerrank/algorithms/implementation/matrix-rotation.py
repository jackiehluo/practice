def rotate(matrix, m, n, rotations):
    layers = int(min(n, m) / 2)
    ring = [[] for layer in range(layers)]
    for level in range(layers):
        top = n - 1 - level * 2
        side = m - 1 - level * 2
        for row in range(top):
            ring[level].append(matrix[level][level + row])
        for col in range(side):
            ring[level].append(matrix[level + col][level + top])
        for row in range(top):
            ring[level].append(matrix[level + side][level + top - row])
        for col in range(side):
            ring[level].append(matrix[level + side - col][level])
    for level in range(layers):
        r = rotations % len(ring[level])
        ring[level] = ring[level][r:] + ring[level][:r]
    for level in range(layers):
        top = n - 1 - level * 2
        side = m - 1 - level * 2
        for row in range(top):
            matrix[level][level + row] = ring[level].pop(0)
        for col in range(side):
            matrix[level + col][level + top] = ring[level].pop(0)
        for row in range(top):
            matrix[level + side][level + top - row] = ring[level].pop(0)
        for col in range(side):
            matrix[level + side - col][level] = ring[level].pop(0)
    return matrix

m, n, rotations = map(int, raw_input().split())
matrix = []
for _ in range(m):
    matrix.append(list(map(int, raw_input().split())))
matrix = rotate(matrix, m, n, rotations)
for row in matrix:
    print " ".join(map(str, row))