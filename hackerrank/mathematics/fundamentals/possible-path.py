from fractions import gcd

t = int(raw_input())
for _ in range(t):
    a, b, x, y = map(int, raw_input().split())
    if (gcd(abs(a), abs(b)) == gcd(abs(x), abs(y))):
        print "YES"
    else:
        print "NO"
