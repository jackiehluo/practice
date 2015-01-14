def get_decent(digits):
    target = digits
    threes = 0
    fives = 0
    max = 0
    while digits > 0:
        if digits % 3 == 0:
            fives = digits
            break
        digits -= 5
    threes = target - digits
    if digits < 0 or threes % 5 != 0:
        return "-1"
    number = ""
    while fives > 0:
        number += "5"
        fives -= 1
    while threes > 0:
        number += "3"
        threes -= 1
    return number

test_cases = (int)(raw_input())

for i in range(test_cases):
    digits = (int)(raw_input())
    answer = get_decent(digits)
    print answer