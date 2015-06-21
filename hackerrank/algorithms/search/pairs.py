def pairs(a,k):
    numbers = set(a)
    answer = sum(1 for i in a if i - k in numbers)
    return answer

if __name__ == '__main__':
    a = map(int, raw_input().strip().split(" "))
    _a_size=a[0]
    _k=a[1]
    b = map(int, raw_input().strip().split(" "))
    print pairs(b,_k)
