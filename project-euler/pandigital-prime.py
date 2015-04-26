from math import sqrt

def prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    else:
        for div in range(3, int(sqrt(n)) + 1, 2):
            if n % div == 0:
                return False
        return True

for i in range(7654321, 1, -2):
    if prime(i):
        pan = "".join([str(j) for j in range(1, len(str(i)) + 1)])
        if "".join(sorted(str(i))) == pan:
            print i
            break