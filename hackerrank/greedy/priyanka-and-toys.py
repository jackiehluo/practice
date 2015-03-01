def buy_toys(weights):
    weights.sort()
    cart = set()
    units = 0
    for w in weights:
        if w not in cart:
            for i in range(w, w + 5):
                if i in weights:
                    cart.add(i)
            units += 1
    return units

n = int(raw_input())
weights = [int(x) for x in raw_input().split()]
answer = buy_toys(weights)
print answer
