from collections import Counter
from math import factorial

def count_jokes(cal):
    jokes = 0
    if cal:
        count = Counter(cal)
        for k in count:
            if count[k] > 1:
                jokes += nCr(count[k], 2)
    print jokes
    
def nCr(n, r):
    f = factorial
    return f(n) / f(r) / f(n - r)

n = int(raw_input())
cal = []

for num in range(n):
    x, y = raw_input().split()
    if set(y) <= set(str(range(int(x)))):
        cal.append(int(y, int(x)))

count_jokes(cal)
