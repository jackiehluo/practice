from itertools import product

def special_multiple(n):
    if n in m:
        return m[n]
    else:
        for i in product("09", repeat = int(round(n / 2)) + len(str(n))):
            a = int("".join(map(str, i)))
            if(a != 0 and a % n == 0):
                m[n] = a
                return a

t = int(raw_input())
m = {1 : 9}

for case in range(t):
    n = int(raw_input())
    print special_multiple(n)