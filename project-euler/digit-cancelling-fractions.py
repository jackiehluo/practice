fractions = []

for i in range(10, 100):
    for j in range(10, 100):
        if float(i) / float(j) < 1:
            if str(i)[0] == str(j)[1] and not str(j)[0] == "0":
                if float(str(i)[1]) / float(str(j)[0]) == float(i) / float(j):
                    fractions.append([i, j])
            elif str(i)[1] == str(j)[0] and not str(j)[1] == "0":
                if float(str(i)[0]) / float(str(j)[1]) == float(i) / float(j):
                    fractions.append([i, j])

print fractions