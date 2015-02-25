from itertools import combinations_with_replacement

def get_strings(n, m):
    letters = list(map(chr, range(97, 97 + m + 1)))
    total = 0
    count = 0
    for i in combinations_with_replacement(letters, n):
        total += 1
        for j in range(1, n - 1):
            if i[j] == i[j + 1]:
                break
            elif i[j - 1] == i[j + 1]:
                break
            else:
                count += 1
    print total
    return count

test_cases = int(raw_input())

for case in range(test_cases):
    n, m = (int(x) for x in raw_input().split())
    answer = get_strings(n, m)
    print answer % (10 ** 9 + 7)