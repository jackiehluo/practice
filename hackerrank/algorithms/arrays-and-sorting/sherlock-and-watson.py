def rotate(n, k, numbers):
    if k <= n:
        rotated_list = numbers[-k:]
        rotated_list += numbers[:n - k]
        return rotated_list
    else:
        for i in range(k):
            rotated_list = []
            rotated_list.append(numbers[n - 1])
            del numbers[n - 1]
            rotated_list += numbers
            numbers = rotated_list
        return numbers

def query(q, numbers):
    for j in range(q):
        index = int(raw_input())
        print numbers[index]

n, k, q = (int(x) for x in raw_input().split())
numbers = [int(y) for y in raw_input().split()]
numbers = rotate(n, k, numbers)
query(q, numbers)