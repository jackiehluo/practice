def anti_vowel(text):
    for letter in text:
        for vowel in "aeiouAEIOU":
            if letter == vowel:
                text = text.replace(letter, "")
    return text