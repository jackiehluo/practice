f = open('day2.txt', 'r')
total = 0
for line in f:
    l, w, h = map(int, line.split('x'))
    sa = (2 * l * w) + (2 * w * h) + (2 * h * l)
    slack = min((l * w), (w * h), (h * l))
    total += sa + slack
print total