import sys

a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()

if sorted(a) == sorted(b):
    print "Permutation."
else:
    print "Not a permutation."