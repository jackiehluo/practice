from math import floor, log

def play_game(n):
    turns = 0
    while n > 1:
        turns += 1
        if log(n, 2).is_integer():
            n /= 2
        else:
            n -= 2 ** int(floor(log(n, 2)))
    if turns % 2 == 0:
        return "Richard"
    else:
        return "Louise"
            
t = int(raw_input())

for _ in range(t):
    n = int(raw_input())
    print play_game(n)
