f = open('day5.txt', 'r')

def three_vowels(string):
    vowels = 'aeiou'
    count = 0
    for c in string:
        if c in vowels:
            count += 1
    return count > 2

def double_letters(string):
    for i in range(1, len(string)):
        if string[i - 1] == string[i]:
            return True
    return False

def no_bad_substrings(string):
    return (('ab' not in string) and
            ('cd' not in string) and
            ('pq' not in string) and
            ('xy' not in string))

count = 0
for line in f:
    if (three_vowels(line) and
        double_letters(line) and
        no_bad_substrings(line)):
        count += 1
print count