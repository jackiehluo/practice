def is_palindrome(s):
    return s == s[::-1]
    
s = list(raw_input())
c = []

while not is_palindrome(s):
    c.append(s.pop())

print len(s) + len(c) * 2
