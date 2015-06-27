from collections import OrderedDict

n = int(raw_input())
words = OrderedDict()

for _ in range(n):
    s = raw_input()
    if s in words:
        words[s] += 1
    else:
        words[s] = 1

print len(words)
print ' '.join(map(str, words.values()))