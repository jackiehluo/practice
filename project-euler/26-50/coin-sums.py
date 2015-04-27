total = 200
values = [1, 2, 5, 10, 20, 50, 100, 200]
ways = [0] * 201
ways[0] = 1

for i in range(len(values)):
    for j in range(values[i], total + 1):
        ways[j] += ways[j - values[i]]

print ways[200]