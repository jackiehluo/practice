def fill_jug(a, b, c):
    h, l, d = max(a, b), min(a, b), abs(a - b)
    if a == c and b == c:
        return True
    while d > 0:
        if d == c:
            return True
        elif d < l:
            d = h - l + d
        elif d >= l:
            d -= l
    return False

t = int(raw_input())
for _ in range(t):
    a, b, c = map(int, raw_input().split())
    if fill_jug(a, b, c):
        print "YES"
    else:
        print "NO"
