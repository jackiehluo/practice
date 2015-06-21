def find_substring(first, second):
    short_first = set(first)
    short_second = set(second)
    for i in short_first:
        if i in short_second:
            return "YES"
    return "NO"

test_cases = int(raw_input())

for case in range(test_cases):
    first = raw_input()
    second = raw_input()
    answer = find_substring(first, second)
    print answer