from math import ceil, sqrt

def find_stations(r, k):
    count = 0
    for i in range(int(ceil(sqrt(r)))):
        if sqrt(r - i ** 2) == int(sqrt(r - i ** 2)):
            count += 4
            if count > k:
                return "impossible"
    return "possible"

test_cases = int(raw_input())

for case in range(test_cases):
    r, k = (int(x) for x in raw_input().split())
    answer = find_stations(r, k)
    print answer
