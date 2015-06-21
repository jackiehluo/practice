def check_elements(number, array):
    element = "NO"
    if len(array) == 1:
        element = "YES"
        return element
    first = 0
    second = sum(array) - array[0]
    for j in range(1, number):
        first += array[j - 1]
        second -= array[j]
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