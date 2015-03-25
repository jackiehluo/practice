colors = ["White", "Black", "Blue", "Red", "Yellow"]
not_colors = []

n = int(raw_input())

for c in range(n):
    color = raw_input()
    if color not in not_colors:
        not_colors.append(color)

for item in colors:
    if item not in not_colors:
        print item
