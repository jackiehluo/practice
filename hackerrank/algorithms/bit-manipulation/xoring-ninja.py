import operator
from itertools import combinations

def xor(numbers):
    total = reduce(operator.or_, numbers) % 1000000007
    for _ in range(len(numbers) - 1):
        total <<= 1
        total %= 1000000007
    return total

t = int(raw_input())

for _ in range(t):
    n = int(raw_input())
    numbers = [int(x) for x in raw_input().split()]
    print xor(numbers)