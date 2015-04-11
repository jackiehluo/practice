from collections import Counter

f = open('pokemon', 'r')

names = []

for line in f:
    names.append(line)

max_length = 0
pokemon = ''

for i in range(len(names)):
    p = [names[i]]
    start = names[i][-2]
    shiritori = True
    count = 1
    while shiritori == True:
        shiritori = False
        for j in range(len(names)):
            if i != j and names[j][0] == start and not names[j] in p:
                count += 1
                start = names[j][-2]
                shiritori = True
                p.append(names[j])
                if count > max_length:
                    max_length = count
                    pokemon = names[i]
                break
    print p

print pokemon + str(max_length)