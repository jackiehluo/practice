def buy_gifts(b, w, x, y, z):
    if (x == y) or (x <= y + z and y <= x + z):
        return b * x + w * y
    elif x > y + z:
        return b * (y + z) + w * y
    elif y > x + z:
        return b * x + w * (x + z)     
        
t = int(raw_input())

for case in range(t):
    b, w = (int(x) for x in raw_input().split())
    x, y, z = (int(y) for y in raw_input().split())
    cost = buy_gifts(b, w, x, y, z)
    print cost
