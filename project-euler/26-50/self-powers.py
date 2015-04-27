total = 0
mod = 100000000000

for i in range(1, 1001):
    total += i ** i % mod

print str(total)[-10:]