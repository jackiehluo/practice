n = int(raw_input())
orders = []

for num in range(n):
    t, d = (int(x) for x in raw_input().split())
    orders.append([t + d, num + 1])

orders.sort()
answer = ""

for o in orders:
    answer += str(o[1]) + " "
    
print answer
