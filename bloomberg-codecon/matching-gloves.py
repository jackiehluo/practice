from collections import Counter

words = []

for _ in range(int(raw_input())):
    words.append(raw_input())

pairs = 0
counts = Counter(words)

for k, v in counts.items():
    if k == k[::-1]:
        continue
    if k[::-1] in counts and counts[k] == counts[k[::-1]]:
        pairs += v / 2.0
    else:
        pairs = -1
        break
    
print int(pairs)
