from math import factorial

def nCr(n, r):
    f = factorial
    return f(n) / f(r) / f(n - r)

test_cases = int(raw_input())

for case in range(test_cases):
    zeroes, ones = (int(x) for x in raw_input().split())
    n = zeroes + (ones - 1)
    answer = nCr(n, zeroes)
    print (answer % (10 ** 9 + 7))