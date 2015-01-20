#!/bin/python
def insertionSort(ar):
    for j in range(1, len(ar)):
        number = ar[j]
        previous = j - 1
        while previous >= 0 and ar[previous] > number:
            ar[previous + 1] = ar[previous]
            previous = previous - 1
        ar[previous + 1] = number
        print ' '.join(map(str, ar))

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)