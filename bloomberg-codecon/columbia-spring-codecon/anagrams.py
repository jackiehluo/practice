def find_anagrams(s, w):
    anagrams = []
    w.lower()
    for i in range(0, len(s) - len(w)):
        sub = s[i:i + len(w)]
        if sorted(sub.lower()) == sorted(w) and sub.lower() != w:
            anagrams.append(sub)
    return sorted(anagrams)

s = raw_input()
w = raw_input()
anagrams = find_anagrams(s, w)
for anagram in anagrams:
    print anagram
