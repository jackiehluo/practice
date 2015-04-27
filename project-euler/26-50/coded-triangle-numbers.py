f = open('words.txt', 'r')

for line in f:
    words = [s[1:-1] for s in line.split(',')]

triangles = [int(0.5 * i * (i + 1)) for i in range(1, 100000)]

triangle_words = 0

for word in words:
    total = 0
    for c in word:
        total += ord(c) - 64
    if total in triangles:
        triangle_words += 1

print triangle_words