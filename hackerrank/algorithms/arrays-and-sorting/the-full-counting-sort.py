def add_dashes(length, words):
    for y in range(length / 2):
        words[y] = "-"
    return words

def sort_numbers(length, numbers, words):
    ordered_words = ["-"] * length
    indexes = [i[0] for i in sorted(enumerate(numbers), key = lambda x:x[1])]
    for z in range(length):
        previous = indexes[z]
        ordered_words[z] = words[previous]
    return ordered_words

length = int(raw_input())
numbers = []
words = []

for x in range(length):
    number, word = raw_input().split()
    numbers.append(int(number))
    words.append(word)

words = add_dashes(length, words)
ordered_words = sort_numbers(length, numbers, words)
print ' '.join(map(str, ordered_words))