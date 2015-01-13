def censor(text, word):
    new_text = text.split()
    i = 0
    for part in new_text:
        if part == word:
            new_text[i] = "*" * len(word)
        i += 1
    return " ".join(new_text)