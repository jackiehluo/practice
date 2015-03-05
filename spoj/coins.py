import sys

def convert(n):
    if n in memo:
        return memo[n]
    else:
    	memo[n] = max(n, convert(n / 2) + convert(n / 3) + convert(n / 4))
        return memo[n]

memo = {0 : 0}

for line in sys.stdin:
    coin = int(line)
    answer = convert(coin)
    print answer