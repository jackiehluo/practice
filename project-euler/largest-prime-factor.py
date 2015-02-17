n = 600851475143
i = 2

while i ** 2 <= n:
    if n % i:
        i += 1
    else:
        n //= i
print n