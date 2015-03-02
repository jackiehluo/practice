from math import sqrt

def find_primes(n):
    root = int(sqrt(n))
    sieve = [True] * (n + 1)
    sieve[0] = False
    sieve[1] = False
    sieve[4:n + 1:2] = [False] * (n / 2 - 1)
    for i in xrange(2, root + 1):
        if sieve[i]:
            m = (n / i - i) / 2
            sieve[i * i:n + 1:i + i] = [False] * (m + 1)
    sieve = [i for i in xrange(n + 1) if sieve[i]]
    return sieve

t = int(raw_input())

for case in range(t):
    m, n = (int(x) for x in raw_input().split())
    answer = find_primes(n)
    index = next(x[0] for x in enumerate(answer) if x[1] >= m)
    print "\n".join(map(str, answer[index:]))
    if case != t - 1:
        print