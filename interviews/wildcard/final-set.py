generation = [9, 10, 21, 20, 7, 11, 4, 15, 7, 7, 14, 5, 20, 6, 29, 8, 11, 19, 18, 22, 29, 14, 27, 17, 6, 22, 12, 18, 18, 30]
overhead = [21, 16, 19, 26, 26, 7, 1, 8, 17, 14, 15, 25, 20, 3, 24, 5, 28, 9, 2, 14, 9, 25, 15, 13, 15, 9, 6, 20, 27, 22]
budget = 2912

sorted_lists = sorted(zip(generation, overhead), key=lambda x: x[1])
generation, overhead = [[x[i] for x in sorted_lists] for i in range(2)]
i = 0
total = 0

while total <= 2912:
    i += 1
    total = 0
    for x in range(i):
        total += generation[x] + overhead[x] * (i - 1)
    print total, i