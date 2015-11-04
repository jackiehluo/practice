import math

def divide1(n, divisor):
    quotient = int(math.exp(math.log(n) - math.log(divisor)))
    remainder = int(n - quotient * divisor)
    return quotient, remainder

def divide2(n, divisor):
    quotient = 0
    while n >= divisor:
        n -= divisor
        quotient += 1
    remainder = n
    return quotient, remainder