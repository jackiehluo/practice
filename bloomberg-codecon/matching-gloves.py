from collections import Counter

n = int(raw_input())
words = []

for _ in range(n):
    words.append(raw_input())

pairs = 0
counts = Counter(words)

for k, v in counts.items():
    if k == k[::-1]:
        continue
    if k[::-1] in counts:
        if counts[k] == counts[k[::-1]]:
            pairs += v / 2.0
        else:
            pairs = -1
            break
    
print int(pairs)
