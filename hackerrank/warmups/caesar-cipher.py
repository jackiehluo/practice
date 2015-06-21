n = int(raw_input())
s = raw_input()
k = int(raw_input())

encryption = ""
k %= 26

for c in s:
    if c.isalpha() and c.isupper() and ord(c) + k > 90:
        encryption += chr(ord(c) - 26 + k)
    elif c.isalpha() and c.islower() and ord(c) + k > 122:
        encryption += chr(ord(c) - 26 + k)
    elif c.isalpha():
        encryption += chr(ord(c) + k)
    else:
        encryption += c

print encryption