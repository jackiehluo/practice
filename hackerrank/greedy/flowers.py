#!/bin/python

def buy_flowers(n, k, c):
    if n <= k:
        cost = sum(c)
    else:
        c.sort(reverse = True)
        cost = sum(c[:k])
        i = 1
        j = 0
        for price in c[k:]:
            cost += (i + 1) * price
            j += 1
            if j % k == 0:
                i += 1
    return cost

n, k = (int(x) for x in raw_input().split())
c = [int(y) for y in raw_input().split()]

answer = buy_flowers(n, k, c)
print answer
