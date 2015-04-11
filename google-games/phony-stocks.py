from collections import Counter

f = open('stocks', 'r')
nums = []

for line in f:
    num = ''
    for c in line:
        if c == 'A' or c == 'B' or c == 'C':
            num += '2'
        elif c == 'D' or c == 'E' or c == 'F':
            num += '3'
        elif c == 'G' or c == 'H' or c == 'I':
            num += '4'
        elif c == 'J' or c == 'K' or c == 'L':
            num += '5'
        elif c == 'M' or c == 'N' or c == 'O':
            num += '6'
        elif c == 'P' or c == 'Q' or c == 'R' or c == 'S':
            num += '7'
        elif c == 'T' or c == 'U' or c == 'V':
            num += '8'
        elif c == 'W' or c == 'X' or c == 'Y' or c == 'Z':
            num += '9'
    nums.append(num)

counts = Counter(nums)
total = 0

for k, v in counts.iteritems():
    if v == 1:
        total += 1

print total