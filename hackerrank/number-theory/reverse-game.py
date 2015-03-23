t = int(raw_input())

for case in range(t):
    n, k = (int(x) for x in raw_input().split())
    if k < n / 2:
        print k * 2 + 1
    else:
        print (n - k - 1) * 2