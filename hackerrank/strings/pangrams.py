from collections import Counter
import string

def check_pangram(text):
    alphabet = list(string.ascii_lowercase)
    counts = Counter(text)
    letters = sorted(list(counts.keys()))
    if letters == alphabet:
        return "pangram"
    else:
        return "not pangram"

sentence = raw_input().lower()
text = list("".join(sentence.split()))
answer = check_pangram(text)
print answer