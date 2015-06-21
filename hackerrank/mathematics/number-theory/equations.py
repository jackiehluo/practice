def find_primes(n):
    sieve = [False, False] + [True] * (n - 1)
    zeroes = [False] * (len(sieve) / 2)
    for i in xrange(2, int(len(sieve) ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i::i] = zeroes[:((len(sieve) - 1) / i) - i + 1]
    return [index for index, i in enumerate(sieve) if i]

def find_power(p, n):
    power = 0
    while n != 0:
        power += n / p
        n /= p
    return power

def count(n):
    mod = 1000007
    primes = find_primes(n)
    a = 1
    for p in primes:
        power = find_power(p, n)
        a = ((a % mod) * (power * 2 + 1) % mod) % mod
    return a
        
n = int(raw_input())
print count(n)