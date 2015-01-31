def swap(numbers):
    size = len(numbers)
    sorted_numbers = sorted(numbers)
    for i in range(size):
        for j in range(size):
            if i != j:
                temp = list(numbers)
                temp[i], temp[j] = temp[j], temp[i]
                if temp == sorted_numbers:
                    print "yes"
                    print "swap " + str(i + 1) + " " + str(j + 1)
                    return True
    return False

def reverse(numbers):
    size = len(numbers)
    sorted_numbers = sorted(numbers)
    for k in range(size):
        for l in range(size):
            if k < l:
                temp = list(numbers)
                temp[k:(l + 1)] = reversed(temp[k:(l + 1)])
                if temp == sorted_numbers:
                    print "yes"
                    print "reverse " + str(k + 1) + " " + str(l + 1)
                    return True
    return False

size = int(raw_input())
numbers = [int(x) for x in raw_input().split()]
match = False
sorted_numbers = sorted(numbers)

if numbers == sorted_numbers:
    match = True
    print "yes"
else:
    match = swap(numbers)
    if not match:
        match = reverse(numbers)
        if not match:
            print "no"