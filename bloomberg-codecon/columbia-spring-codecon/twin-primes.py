from math import sqrt

def twin_primes(n):
    for i in range(n, 0, -1):
        prime1 = True
        for j in range(2, int(sqrt(i)) + 1):
            if i % j == 0:
                prime1 = False
        if prime1 == True:
            prime2 = True
            for k in range(2, int(sqrt(i - 2)) + 1):
                if (i - 2) % k == 0:
                    prime2 = False
            if prime2 == True:
                return str(i - 2) + "," + str(i)

k = int(raw_input())
print twin_primes(k)
