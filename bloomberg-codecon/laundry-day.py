import sys
from collections import Counter

clothing = []

for item in sys.stdin:
    clothing.append(item)

counts = Counter(clothing)

for k, v in sorted(counts.items()):
    if 'sock' in k:
        if v / 2 > 0:
            print str(v / 2) + '|' + k
        if v % 2 == 1:
            print '0' + '|' + k
    else:
        print str(v) + '|' + k
