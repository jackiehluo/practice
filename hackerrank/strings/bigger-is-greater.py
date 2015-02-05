def make_bigger(word):
    i = len(word) - 2
    while not (i < 0 or word[i] < word[i + 1]):
        i -= 1
    if i < 0:
        return "no answer"
    j = len(word) - 1
    while not (word[j] > word[i]):
        j -= 1
    word[i], word[j] = word[j], word[i]
    word[i + 1:] = reversed(word[i + 1:])
    return "".join(map(str, word))

test_cases = int(raw_input())

for case in range(test_cases):
    word = list(raw_input())
    answer = make_bigger(word)
    print answer