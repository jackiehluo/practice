from itertools import permutations
from math import sqrt

def prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    else:
        for div in range(2, int(sqrt(n)) + 1):
            if n % div == 0:
                return False
        return True

n = set()

for i in range(1001, 10000, 2):
    if i not in n:
        perms = set([''.join(p) for p in permutations(str(i)) if p[0] != '0'])
        sequence = []
        for j in perms:
            n.add(int(j))
            if prime(int(j)):
                sequence.append(int(j))
        sequence.sort()
        for k in range(len(sequence)):
            for l in range(k + 1, len(sequence)):
                if (sequence[l] + sequence[l] - sequence[k]) in sequence:
                    print sequence[k], sequence[l], (sequence[l] + sequence[l] - sequence[k])
                    break