def make_palindrome(text):
    reverse = text[::-1]
    length = len(text)
    if text == reverse:
        return "-1"
    else:
        for letter in range(length):
            if text[letter] != reverse[letter]:
                first_text = text[:letter] + text[letter + 1:]
                first_reverse = first_text[::-1]
                second_text = text[:length - letter] + text[length - letter + 1:]
                second_reverse = second_text[::-1]
                if first_text == first_reverse:
                    return str(letter)
                elif second_text == second_reverse:
                    return str(length - letter)

test_cases = int(raw_input())

for case in range(test_cases):
    text = raw_input()
    answer = make_palindrome(text)
    print answer