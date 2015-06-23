n = int(raw_input())
l = []

for _ in range(n):
    command = raw_input().split()
    if "insert" in command:
        l.insert(int(command[1]), int(command[2]))
    elif "append" in command:
        l.append(int(command[1]))
    elif "remove" in command:
        l.remove(int(command[1]))
    elif "pop" in command:
        l.pop()
    elif "index" in command:
        l.index(int(command[1]))
    elif "count" in command:
        l.count(int(command)[1])
    elif "sort" in command:
        l.sort()
    elif "reverse" in command:
        l.reverse()
    else:
        print l