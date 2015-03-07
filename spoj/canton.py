from math import sqrt

t = int(raw_input())

for case in range(t):
    n = int(raw_input())
    a = float(sqrt(1 + 8 * (n - 1)))
    b = int((a + 1) / 2)
    c = int((b * (b - 1)) / 2)
    d = n - c
    if b % 2 == 0:
        print "TERM " + str(n) + " IS " + str(d) + "/" + str(b + 1 - d)
    
    else:
        print "TERM " + str(n) + " IS " + str(b + 1 - d) + "/" + str(d)
