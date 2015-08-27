import sys

def unique(s):
    char = [False] * 128
    if len(s) > 128:
        return False
    for c in s:
        if char[ord(c)] == True:
            return False
        else:
            char[ord(c)] = True
    return True

s = sys.stdin.readline().strip()
if unique(s):
    print "Unique."
else:
    print "Not unique."