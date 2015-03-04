def ap_or_gp(numbers):
    if numbers[1] - numbers[0] == numbers[2] - numbers[1]:
        print "AP " + str((numbers[1] - numbers[0]) + numbers[2])
    elif numbers[1] / numbers[0] == numbers[2] / numbers[1]:
        print "GP " + str((numbers[1] / numbers[0]) * numbers[2])

run = True

while run == True:
    numbers = [int(x) for x in raw_input().split()]
    if numbers == [0, 0, 0]:
        break
        run = False
    ap_or_gp(numbers)