from itertools import product

def get_strings(n, m):
    letters = list(map(chr, range(97, 97 + m)))
    count = 0
    for i in product(letters, repeat = n):
        if n <= 2:
            if n == 1:
                palindrome = False
            elif n == 2:
                if i[0] == i[1]:
                    palindrome = True
                else:
                    palindrome = False
        else:
            for j in range(0, n - 2):
                if i[j] == i[j + 1] or i[j + 1] == i[j + 2]:
                    palindrome = True
                    break
                elif i[j] == i[j + 2]:
                    palindrome = True
                    break
                else:
                    palindrome = False
        if palindrome == False:
            count += 1
    return count

test_cases = int(raw_input())

for case in range(test_cases):
    n, m = (int(x) for x in raw_input().split())
    answer = get_strings(n, m)
    print answer % (10 ** 9 + 7)