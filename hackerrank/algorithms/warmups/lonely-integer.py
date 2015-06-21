#!/usr/bin/py

def lonelyinteger(a):
    a.sort()
    for i in range(len(a)):
        if a.count(a[i]) == 1:
            answer = a[i]
    return answer

if __name__ == '__main__':
    a = input()
    b = map(int, raw_input().strip().split(" "))
    print lonelyinteger(b)