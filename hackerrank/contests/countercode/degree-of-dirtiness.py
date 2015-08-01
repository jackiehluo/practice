for _ in range(int(raw_input())):
    n, m = map(int, raw_input().split())
    toilets = [0] * n
    for i in xrange(m):
        l = min(toilets)
        if i % 2 == 0:
            a = 0
            while toilets[a] > l:
                a += 1
        else:
            a = n - 1
            while toilets[a] > l:
                a -= 1
        if i == m - 1:
            print a + 1, toilets[a]
        else:
            toilets[a] += 1