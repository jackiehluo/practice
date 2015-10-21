def move_disks(n, start, middle, end):
    if n > 0:
        move_disks(n - 1, start, end, middle)
        if start:
            end.append(start.pop())
        move_disks(n - 1, middle, start, end)
        
start = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
middle = []
end = []
move_disks(len(start), start, middle, end)