def anagrams(s):
    count = {}
    for i in range(len(s)):
        for j in range(i, len(s)):
            sub = "".join(sorted(s[i:j + 1]))
            count[sub] = count.get(sub, 0) + 1
    return sum((n * (n - 1)) / 2 for n in count.values())

t = int(raw_input())

for case in range(t):
    s = raw_input()
    print anagrams(s)