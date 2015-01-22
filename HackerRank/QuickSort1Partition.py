#!/bin/python
def partition(ar):
    partition = ar[0]
    first = []
    last = []
    for x in range(1, len(ar)):
        if ar[x] < partition:
            first.append(ar[x])
        if ar[x] > partition:
            last.append(ar[x])
    first.append(partition)
    combined = first + last
    return combined

m = input()
ar = [int(i) for i in raw_input().strip().split()]
ar = partition(ar)
print ' '.join(map(str, ar))
