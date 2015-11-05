import re

dictionary = open("wordlist.txt", "r")
words = []

for word in dictionary:
    if re.match("(?<!\S)[jackieluo]+(?!\S)", word):
        words.append(word.strip())

max_length = max(len(word) for word in words)
print(sorted([word for word in words if len(word) == max_length])[0])
