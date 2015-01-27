import math

def slice(cuts):
    horizontal = (int)(math.floor(cuts / 2))
    vertical = (int)(math.ceil(cuts / 2))
    pieces = horizontal * vertical
    return pieces

test_cases = (int)(raw_input())

for i in range(test_cases):
    cuts = (float)(raw_input())
    pieces = slice(cuts)
    print pieces