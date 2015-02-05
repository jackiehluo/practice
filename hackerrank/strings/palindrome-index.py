def make_palindrome(text):
    reverse = text[::-1]
    if text == reverse:
        return "-1"
    else:
        for letter in range(len(text)):
            new_text = text[:letter] + text[letter + 1:]
            new_reverse = new_text[::-1]
            if new_text == new_reverse:
                return str(letter)

test_cases = int(raw_input())

for case in range(test_cases):
    text = raw_input()
    answer = make_palindrome(text)
    print answer