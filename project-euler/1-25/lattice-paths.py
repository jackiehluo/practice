lattice = [1] * 20
for i in range(20):
    for j in range(i):
        lattice[j] = lattice[j] + lattice[j - 1]
    lattice[i] = 2 * lattice[i - 1]
print lattice[19]