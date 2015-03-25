from collections import Counter

s = raw_input()
counts = Counter(s)
palindrome = True
if len(s) % 2 == 0:
    for k, v in counts.iteritems():
        if v % 2 != 0:
            palindrome = False
else:
    count = 0
    for k, v in counts.iteritems():
        if v % 2 != 0:
            count += 1
    if count > 1:
        palindrome = False
if palindrome == True:
    print "yes"
else:
    print "no"
