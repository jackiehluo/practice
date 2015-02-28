def find_primes(m, n):
    for i in range(m, n + 1):
        if i > 1:
            prime = True
            for j in range(2, i):
                if i % j == 0:
                    prime = False
                    break
            if prime == True:
                print i
    print "\n"

t = int(raw_input())

for case in range(t):
    m, n = (int(x) for x in raw_input().split())
    find_primes(m, n)
