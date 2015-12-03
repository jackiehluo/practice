from math import sqrt

for _ in range(int(raw_input())):
    target = int(raw_input())
    triangle = int((sqrt(8 * target + 1) - 1) / 2)
    if triangle * (triangle + 1) / 2 == target:
        print "Go On Bob %s" % (triangle)
    else:
        print "Better Luck Next Time"