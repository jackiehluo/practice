pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    print original
else:
    print 'empty'

word = original.lower()
first = word[0]
new_word = word + first + pyg
new_word = new_word[1:]
print new_word