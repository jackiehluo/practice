def find_palindrome(num):
    palindrome = False
    while palindrome == False:
        num += 1
        l = len(str(num))
        if l % 2 == 0:
            if str(num)[:l / 2 - 1:] == str(num)[l / 2::-1]:
                palindrome = True
                print palindrome
        else:
            if str(num)[:l / 2 - 1:] == str(num)[l / 2 + 1::-1]:
                palindrome = True
                print palindrome

t = int(raw_input())

for case in range(t):
    num = int(raw_input())
    find_palindrome(num)