from math import ceil

run = True

while run == True:
    g, b = (int(x) for x in raw_input().split())
    if g < 0:
        run = False
    else:
        if g == 0 or b == 0:
            print max(g, b)
        elif g == b and g > 0 and b > 0:
            print 1
        else:
            print int(ceil(float(max(g, b)) / float((min(g, b) + 1))))
