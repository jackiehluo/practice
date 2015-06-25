s = raw_input()
n, c = raw_input().split()
print s[:int(n)] + c + s[int(n) + 1:]
