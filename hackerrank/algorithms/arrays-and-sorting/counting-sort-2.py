length = int(raw_input())
numbers = [int(x) for x in raw_input().split()]
numbers.sort()
print ' '.join(map(str, numbers))