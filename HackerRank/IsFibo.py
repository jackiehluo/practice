import math

def check_fibo(number):
    a = 5 * number ** 2 + 4
    b = 5 * number ** 2 - 4
    if (a == int(math.sqrt(a)) ** 2) or (b == int(math.sqrt(b)) ** 2):
        return "IsFibo"
    else:
        return "IsNotFibo"
    
test_cases = (int)(raw_input())

for i in range(test_cases):
    number = (int)(raw_input())
    answer = check_fibo(number)
    print answer