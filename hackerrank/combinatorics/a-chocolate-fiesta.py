def find_subsets(evens, odds):
    if odds % 2 == 0:
        subsets = 2 ** (evens + odds - 1)
    else:
        subsets = 2 ** (evens + odds - 1) - 1
    return subsets

size = int(raw_input())
numbers = [int(x) for x in raw_input().split()]
evens = 0
odds = 0

for number in numbers:
    if number % 2 == 0:
        evens += 1
    else:
        odds += 1

answer = find_subsets(evens, odds)
print answer % (10 ** 9 + 7)