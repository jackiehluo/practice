def partition(str, dictionary):
    word_lists = []
    ind = []
    words = []
    i = 0
    j = 1
    while True:
        while i < len(str):
            found = False
            while j <= len(str):
                sub = str[i:j]
                if sub in dictionary:
                    found = True
                    ind.append([i, j])
                    words.append(sub)
                    break
                j += 1
            if found:
                i = j
                j = i + 1
                if i == len(str):
                    word_lists.append(words)
                    last = ind.pop()
                    i = last[0]
                    j = last[1] + 1
                    words = []
            else:
                if ind:
                    last = ind.pop()
                    i = last[0]
                    j = last[1] + 1
                else:
                    break
        if not ind:
            break
    return word_lists

str = "dogsandcat"
dictionary = ["dog", "dogs", "sand", "and", "cat"]
print partition(str, dictionary)