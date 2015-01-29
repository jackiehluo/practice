def check_elements(number, array):
    element = "NO"
    for i in range(number):
        first = 0
        second = 0
        for j in range(i):
            first += array[j]
        for k in range(i + 1, number):
            second += array[k]
        if first == second:
            element = "YES"
            break
    return element
        
test_cases = int(raw_input())

for i in range(test_cases):
    number = int(raw_input())
    array = [int(x) for x in raw_input().split()]
    answer = check_elements(number, array)
    print answer