from collections import Counter

def find_missing_numbers(first, second):
    first_counts = Counter(first)
    second_counts = Counter(second)
    difference = second_counts - first_counts
    missing_numbers = []
    for key, value in difference.iteritems():
        for v in range(value):
            if key not in missing_numbers:
                missing_numbers.append(key)
    answer = sorted(missing_numbers)
    return answer

first_length = int(raw_input())
first = [int(x) for x in raw_input().split()]
second_length = int(raw_input())
second = [int(y) for y in raw_input().split()]
answer = find_missing_numbers(first, second)
print " ".join(map(str, answer))