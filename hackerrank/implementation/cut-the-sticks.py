def cut_sticks(sticks):
    while len(sticks) > 0:
        new_sticks = []
        count = 0
        for i in range(len(sticks)):
            count += 1
            if (sticks[i] - min(sticks)) > 0:
                new_length = sticks[i] - min(sticks)
                new_sticks.append(new_length)
        sticks = new_sticks
        print count

number = int(raw_input())
sticks = [int(x) for x in raw_input().split()]

cut_sticks(sticks)