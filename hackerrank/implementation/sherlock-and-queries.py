from collections import defaultdict

def perform_program(n, m, a, b, c):
    factors = defaultdict(one)
    for i in range(0, m):
        factors[b[i]] = factors[b[i]] * c[i] % 1000000007
    for i, factor in factors.iteritems():
        for j in xrange(i - 1, n, i):
            a[j] = a[j] * factor % 1000000007
    return a
    
def one():
    return 1

n, m = (int(w) for w in raw_input().split())
a = [int(x) for x in raw_input().split()]
b = [int(y) for y in raw_input().split()]
c = [int(z) for z in raw_input().split()]

answer = perform_program(n, m, a, b, c)
print ' '.join(map(str, answer))
