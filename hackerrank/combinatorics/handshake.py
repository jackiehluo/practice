def shake_hands(people):
    sum = 0
    for i in range(people):
        sum += i
    return str(sum)

test_cases = int(raw_input())

for case in range(test_cases):
    people = int(raw_input())
    answer = shake_hands(people)
    print answer