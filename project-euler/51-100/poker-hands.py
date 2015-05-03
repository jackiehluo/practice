from collections import defaultdict

def is_royal_flush(hand):
    v = set(["10", "J", "Q", "K", "A"])
    s = hand[0][-1]
    for c in hand:
        if c[-1] != s:
            return False
        if c[:-1] not in v:
            return False
        else:
            v.remove(c[:-1])
    return True

def is_straight_flush(hand):
    v = {"2", : 2, "3" : 3, "4" : 4, "5" : 5,
        "6" : 6, "7" : 7, "8" : 8, "9" : 9, "10" : 10,
        "J" : 11, "Q" : 12, "K" : 13, "A" : 14}
    n = []
    s = hand[0][-1]
    for c in hand:
        if c[-1] != s:
            return False
        n.append(v[c[:-1]])
    diff = [j - i for i, j in zip(sorted(n)[:-1], sorted(n)[1:])]
    return (sum(diff) / 5.0) == 1

def is_four_of_a_kind(hand):
    k = hand[0][:-1]
    counts = defaultdict(int)
    for c in hand:
        counts[c[:-1]] += 1
    for k, v in counts.iteritems():
        if v == 4:
            return True
    return False

def is_full_house(hand):
    k = hand[0][:-1]
    counts = defaultdict(int)
    for c in hand:
        counts[c[:-1]] += 1
    for k, v in counts.iteritems():
        if v < 2:
            return False
    return False

f = open('poker.txt', 'r')

game = []

for line in f:
    first_hand = map(str, line.split())[:5]
    second_hand = map(str, line.split())[5:]
    game.append([first_hand, second_hand])

for g in game:
