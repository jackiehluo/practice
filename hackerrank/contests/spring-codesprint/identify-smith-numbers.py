def smith(n):
    if(factors(n) == digits(n)):
        return 1
    else:
        return 0

def factors(n):
    f = primes(n)
    s = 0
    for factor in f:
        if factor >= 10:
            s += digits(factor)
        else:
            s += factor
    return s

def digits(n):
    s = 0  
    if n >= 10:
        while n >= 10:
            s += n % 10
            n /= 10
        s += n
        return s
    else:
        return n

def primes(n):
    primes = []
    factor = min_prime(n)
    c = n
    while factor != -1:
        primes.append(factor)
        c /= factor
        factor = min_prime(c)
    if(c != n):
        primes.append(c)
    return primes

def min_prime(n):
    for i in range(2, n / 2 + 1):
        if(n % i == 0):
            return i
    return -1

n = int(raw_input())
print smith(n)
