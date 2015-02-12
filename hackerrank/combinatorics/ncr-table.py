from math import factorial

def nCr(n, r):
    f = factorial
    return f(n) / f(r) / f(n - r)

test_cases = int(raw_input())

for case in range(test_cases):
    n = int(raw_input())
    answer = []
    for x in range(n + 1):
        number = nCr(n, x)
        answer.append(number % (10 ** 9))
    print " ".join(map(str, answer))