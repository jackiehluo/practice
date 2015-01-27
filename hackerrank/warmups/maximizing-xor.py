#!/bin/python

def  maxXor( l,  r):
    max = 0
    for number in range(l, r + 1):
        for second_number in range (l, r + 1):
            new_number = number ^ second_number
            if new_number > max:
                max = new_number
    return max

    
_l = int(raw_input());

_r = int(raw_input());

res = maxXor(_l, _r);
print(res)