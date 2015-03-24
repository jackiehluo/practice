def euler(a, p, m):
    if p == 0:
        return 1
    elif p == 1:
        return a % m
    else:
        answer = euler(a, p / 2, m)
        if p % 2 == 1:
            t = (answer * answer) % m
            t *= a % m
            return t % m
        else:
            return (answer * answer) % m

t = int(raw_input())

for case in range(t):
    a, m = (long(x) for x in raw_input().split())
    answer = euler(a, (m - 1) / 2, m)
    if answer == 1 or a == 0 or a == 2:
        print "YES"
    else:
        print "NO"