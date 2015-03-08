def find_palindrome(num):
    palindrome = False
    while palindrome == False:
        num += 1
        l = len(str(num))
        if l % 2 == 0:
            if str(num) == str(num)[::-1]:
                palindrome = True
                print num
        else:
            if str(num) == str(num)[::-1]:
                palindrome = True
                print num

t = int(raw_input())

for case in range(t):
    num = int(raw_input())
    find_palindrome(num)