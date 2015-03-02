t = int(raw_input())

for case in range(t):
    string, substring = (x for x in raw_input().split())
    if substring in string:
        print 1
    else:
        print 0
