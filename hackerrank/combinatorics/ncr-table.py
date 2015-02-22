from math import factorial

def nCr(n, r):
    f = factorial
    return f(n) / f(r) / f(n - r)

test_cases = int(raw_input())

for case in range(test_cases):
    n = int(raw_input())
    first = []
    for x in range((n + 1) / 2 + 1):
        number = nCr(n, x)
        first.append(number % (10 ** 9))
    if first[-1] == first[-2]:
        second = first[-3::-1]
    else:
        second = first[-2::-1]
    answer = first + second 
    print " ".join(map(str, answer))