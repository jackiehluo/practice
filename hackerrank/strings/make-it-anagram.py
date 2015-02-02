from collections import Counter

def make_anagram(first, second):
    first_counts = Counter(first)
    second_counts = Counter(second)
    first_difference = first_counts - second_counts
    second_difference = second_counts - first_counts
    deletions = sum(first_difference.itervalues()) + sum(second_difference.itervalues())
    return deletions

first = sorted(raw_input())
second = sorted(raw_input())

if first == second:
    print "0"
else:
    answer = make_anagram(first, second)
    print answer