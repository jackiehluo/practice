from math import sqrt

def divisors_sum(n):
    return sum(set(reduce(list.__add__,
                ([i, n // i] for i in range(1, int(sqrt(n)) + 1) if n % i == 0)))) - n

def is_abundant(n):
    if n < 12:
        return False
    return divisors_sum(n) > n

def is_abundant_sum(n):
   for i in abundants:
       if i > n:
         return False
       if (n - i) in abundants:
           return True
   return False

abundants = set(x for x in range(1, 28123) if is_abundant(x))
total = 0

for i in range(1, 28123):
    if not is_abundant_sum(i):
        total += i

print total