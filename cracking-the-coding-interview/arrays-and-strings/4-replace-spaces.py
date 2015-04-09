import sys

s = sys.stdin.readline().strip().split()
n = int(sys.stdin.readline())

print "%20".join(map(str, s))