def reverse(text):
    new_string = ""
    for letter in range(len(text) - 1, -1, -1):
        new_string += text[letter]
    return new_string