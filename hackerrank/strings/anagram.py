from collections import Counter

def find_anagram(text):
    m = len(text) / 2
    first = sorted(text[0:m])
    second = sorted(text[m:len(text)])
    if first == second:
        return "0"
    else:
        first_counts = Counter(first)
        second_counts = Counter(second)
        changes = 0
        for key in first_counts:
            if key in second_counts and (first_counts[key] - second_counts[key]) >= 0:
                changes += first_counts[key] - second_counts[key]
            elif key not in second_counts:
                changes += first_counts[key]
        return changes

test_cases = int(raw_input())

for x in range(test_cases):
    text = raw_input()
    if len(text) % 2 == 1:
        print "-1"
    else:
        answer = find_anagram(text)
        print answer