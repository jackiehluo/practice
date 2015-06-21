import sys

def count(n, m):
    mod = 1000000007
    if n == 1:
        return m
    elif n == 2:
        return m * (m - 1) % mod
    else:
        return (m * (m - 1) % mod) * power(n - 2, m - 2, mod) % mod

def power(n, m, mod):
    if n == 0:
        return 1
    count = 1
    while n:
        if n % 2 == 1:
            count = count * m % mod
        m = m ** 2 % mod
        n /= 2
    return count
    
t = int(sys.stdin.readline())

for _ in range(t):
    n, m = (int(x) for x in sys.stdin.readline().split())
    print count(n, m)