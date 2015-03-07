def recover(notes):
    eq = []
    for i in range(0, len(notes), 2):
        if "machula" in notes[i]:
            blot = i
            eq.append(["blot", i])
        else:
            eq.append([int(notes[i]), i])
    if blot == 4:
        eq[2][0] = eq[0][0] + eq[1][0]
    elif blot == 2:
        eq[1][0] = eq[2][0] - eq[0][0]
    else:
        eq[0][0] = eq[2][0] - eq[1][0]
    return eq

t = int(raw_input())

for case in range(t):
    line = raw_input()
    notes = [x for x in raw_input().split()]
    eq = recover(notes)
    print str(eq[0][0]) + " + " + str(eq[1][0]) + " = " + str(eq[2][0])
