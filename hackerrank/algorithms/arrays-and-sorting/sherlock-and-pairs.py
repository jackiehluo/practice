from collections import Counter

def find_pairs(size, numbers):
    counts = Counter(numbers).values()
    pairs = 0
    for i in range(len(counts)):
        if counts[i] > 1:
            pairs += (counts[i] * (counts[i] - 1))
    print pairs

test_cases = int(raw_input())

for case in range(test_cases):
    size = int(raw_input())
    numbers = [int(x) for x in raw_input().split()]
    find_pairs(size, numbers)