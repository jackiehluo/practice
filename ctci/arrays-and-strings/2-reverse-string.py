s = ["h", "e", "l", "l", "o", None]

f = 0
e = len(s) - 2

while f < e:
    s[f], s[e] = s[e], s[f]
    f += 1
    e -= 1

print s