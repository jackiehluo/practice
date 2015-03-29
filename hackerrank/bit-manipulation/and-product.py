import operator

def and_product(a, b):
    numbers = set(range(a, b + 1))
    return reduce(operator.and_, numbers)

t = int(raw_input())

for _ in range(t):
    a, b = (int(x) for x in raw_input().split())
    print and_product(a, b)