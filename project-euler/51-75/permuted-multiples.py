start = 1
found = False
 
while not found:
    start *= 10
    for i in range(start, start * 10 / 6):
        found = True
        for j in range(2, 7):
            if sorted(str(i)) != sorted(str(i * j)):
                found = False
                break
        if found:
            print i
            break