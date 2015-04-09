import sys

s = sys.stdin.readline().strip()
count = 1
answer = ""

for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        count += 1
    else:
        answer += s[i] + str(count)
        count = 1

answer += s[len(s) - 1] + str(count)

if len(s) < len(answer):
    print s
else:
    print answer