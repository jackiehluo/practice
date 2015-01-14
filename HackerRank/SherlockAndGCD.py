from fractions import gcd

def find_gcd(number, array):
    condition = "YES"
    new_array = [reduce(gcd, array)]
    if len(new_array) == 1 and new_array[0] != 1:
        condition = "NO"
    return condition
    
test_cases = (int)(raw_input())

for i in range(test_cases):
    number = (int)(raw_input())
    array = [int(k) for k in raw_input().split()]
    answer = find_gcd(number, array)
    print answer