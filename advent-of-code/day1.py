f = open('day1.txt', 'r')
left, right = 0, 0
while True:
    c = f.read(1)
    if c == '(':
        left += 1
    elif c == ')':
        right += 1
    else:
        break
print left - right