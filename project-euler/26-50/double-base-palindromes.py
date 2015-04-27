total = 0

for i in range(1, 1000000):
    bin = "{0:b}".format(i)
    if str(i) == str(i)[::-1] and bin == bin[::-1]:
        total += i

print total