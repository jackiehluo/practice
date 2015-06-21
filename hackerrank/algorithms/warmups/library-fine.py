d2, m2, y2 = map(int, raw_input().split())
d1, m1, y1 = map(int, raw_input().split())

if y2 > y1:
    print 10000
elif y2 == y1 and m2 > m1:
    print 500 * (m2 - m1)
elif y2 == y1 and m2 == m1 and d2 > d1:
    print 15 * (d2 - d1)
else:
    print 0