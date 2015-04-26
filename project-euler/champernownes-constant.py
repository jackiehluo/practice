i = 1
s = ""

while True:
    s += str(i)
    i += 1
    if len(s) >= 1000000:
        break


product = int(s[0]) * int(s[9]) * int(s[99]) * int(s[999]) * int(s[9999]) * int(s[99999]) * int(s[999999])

print product