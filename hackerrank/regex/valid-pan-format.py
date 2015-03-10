def validate(s):
    for c in range(10):
        if (c < 5 or c == 9) and (not s[c].isalpha() or not s[c].isupper()):
            return "NO"
        elif (c > 4 and c < 9) and not s[c].isdigit():
            return "NO"
    return "YES"

t = int(raw_input())

for case in range(t):
    s = raw_input()
    print validate(s)
