def substring(a, b, c):
    n = len(b)
    m = a
    for i in range(n):
        index = []
        mismatch = 0
        start = i
        pos_b = 0
        pos_c = i
        while pos_c < n: 
            if b[pos_b] != c[pos_c]:
                mismatch += 1
                index.append(pos_c)
                if mismatch == a + 1:
                    mismatch -= 1
                    m = max(m, pos_c - start)
                    start = index[-(a + 1)] + 1
            pos_b += 1
            pos_c += 1
        m = max(m, n - start)
    return m

def max_length(s, p, q):
    return max(substring(s, p, q), substring(s, q, p))

t = int(raw_input())

for case in range(t):
    s, p, q = raw_input().split()
    print max_length(int(s), p, q)