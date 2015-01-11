def palindrome(characters):
    reverse = characters[::-1]
    changes = 0
    for i in range(len(characters)):
        if ord(characters[i]) > ord(reverse[i]):
            while ord(characters[i]) > ord(reverse[i]):
                characters[i] = chr(ord(characters[i]) - 1)
                changes += 1
    return changes

test_cases = (int)(raw_input())

for i in range(test_cases):
    word = raw_input()
    
    characters = []
    for c in word:
        characters.append(c)
        
    changes = palindrome(characters)
    print changes