from math import sqrt
import string

def eight_prime_family(prime, repeat):
    count = 0
    for digit in "0123456789":
        n = int(string.replace(prime, repeat, digit))
        if n > 100000 and is_prime(n):
            count += 1
    return count == 8

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    else:
        for div in range(2, int(sqrt(n)) + 1):
            if n % div == 0:
                return False
        return True

def find_primes(n):
    primes = []
    for i in range(2, n):
        if is_prime(i):
            primes.append(i)
    return primes

for prime in find_primes(1000000):
    if prime > 100000:
        s = str(prime)
        last = s[-1]
        if ((s.count('0') == 3 and eight_prime_family(s, '0')) or
                (s.count('1') == 3 and last != '1' and eight_prime_family(s, '1')) or
                (s.count('2') == 3 and eight_prime_family(s, '2'))):
            print s
