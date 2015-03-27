import operator
from itertools import combinations

def xor(numbers):
    total = sum(numbers)
    for l in range(2, len(numbers) + 1):
        subsets = combinations(numbers, l)
        for s in subsets:
            total = (total + reduce(operator.xor, s, 0)) % 1000000007
    return total

t = int(raw_input())

for _ in range(t):
    n = int(raw_input())
    numbers = [int(x) for x in raw_input().split()]
    print xor(numbers)
