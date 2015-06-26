from collections import Counter
from math import factorial
from operator import mul

s = raw_input()
counts = Counter(s)
pairs, product, odds = 0, 1, 0

for v in counts.values():
    pairs += v / 2
    product *= factorial(v / 2)
    if v % 2 == 1:
        odds += 1

if (len(s) % 2 == 0 and odds == 0) or (len(s) % 2 == 1 and odds == 1):
    print factorial(pairs) / product
else:
    print 0
