from collections import defaultdict

def is_royal_flush(hand):
    v = set(["T", "J", "Q", "K", "A"])
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
    v = {"2" : 2, "3" : 3, "4" : 4, "5" : 5,
        "6" : 6, "7" : 7, "8" : 8, "9" : 9, "T" : 10,
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
    has_three_of_a_kind = False
    has_pair = False
    for k, v in counts.iteritems():
        if v == 3:
            has_three_of_a_kind = True
        elif v == 2:
            has_pair = True
    if has_three_of_a_kind and has_pair:
        return True
    return False

def is_flush(hand):
    s = hand[0][-1]
    for c in hand:
        if c[-1] != s:
            return False
    return True

def is_straight(hand):
    v = {"2" : 2, "3" : 3, "4" : 4, "5" : 5,
        "6" : 6, "7" : 7, "8" : 8, "9" : 9, "T" : 10,
        "J" : 11, "Q" : 12, "K" : 13, "A" : 14}
    n = []
    for c in hand:
        n.append(v[c[:-1]])
    diff = [j - i for i, j in zip(sorted(n)[:-1], sorted(n)[1:])]
    return (sum(diff) / 5.0) == 1

def is_three_of_a_kind(hand):
    k = hand[0][:-1]
    counts = defaultdict(int)
    for c in hand:
        counts[c[:-1]] += 1
    for k, v in counts.iteritems():
        if v == 3:
            return True
    return False

def is_two_pairs(hand):
    k = hand[0][:-1]
    counts = defaultdict(int)
    for c in hand:
        counts[c[:-1]] += 1
    pairs = 0
    for k, v in counts.iteritems():
        if v == 2:
            pairs += 1
    if pairs == 2:
        return True
    return False

def is_one_pair(hand):
    k = hand[0][:-1]
    counts = defaultdict(int)
    for c in hand:
        counts[c[:-1]] += 1
    pairs = 0
    for k, v in counts.iteritems():
        if v == 2:
            return True
    return False

def winning_hand(a, b):
    v = {"2" : 2, "3" : 3, "4" : 4, "5" : 5,
        "6" : 6, "7" : 7, "8" : 8, "9" : 9, "T" : 10,
        "J" : 11, "Q" : 12, "K" : 13, "A" : 14}
    a_values = []
    b_values = []
    for i in range(5):
        a_values.append(v[a[i][:-1]])
        b_values.append(v[b[i][:-1]])
    a_values.sort(reverse = True)
    b_values.sort(reverse = True)
    for j in range(5):
        if a_values[j] > b_values[j]:
            return a
        elif b_values[j] > a_values[j]:
            return b

f = open('poker.txt', 'r')

game = []
player_one = 0
player_two = 0

for line in f:
    first_hand = map(str, line.split())[:5]
    second_hand = map(str, line.split())[5:]
    game.append([first_hand, second_hand])

for g in game:
    first = g[0]
    second = g[1]
    if is_royal_flush(first) or is_royal_flush(second):
        if is_royal_flush(first) and is_royal_flush(second):
            winner = winning_hand(first, second)
            if winner == first:
                player_one += 1
            else:
                player_two += 1
        elif is_royal_flush(first):
            player_one += 1
        else:
            player_two += 1
    elif is_straight_flush(first) or is_straight_flush(second):
        if is_straight_flush(first) and is_straight_flush(second):
            winner = winning_hand(first, second)
            if winner == first:
                player_one += 1
            else:
                player_two += 1
        elif is_straight_flush(first):
            player_one += 1
        else:
            player_two += 1
    elif is_four_of_a_kind(first) or is_four_of_a_kind(second):
        if is_four_of_a_kind(first) and is_four_of_a_kind(second):
            winner = winning_hand(first, second)
            if winner == first:
                player_one += 1
            else:
                player_two += 1
        elif is_four_of_a_kind(first):
            player_one += 1
        else:
            player_two += 1
    elif is_full_house(first) or is_full_house(second):
        if is_full_house(first) and is_full_house(second):
            winner = winning_hand(first, second)
            if winner == first:
                player_one += 1
            else:
                player_two += 1
        elif is_full_house(first):
            player_one += 1
        else:
            player_two += 1
    elif is_flush(first) or is_flush(second):
        if is_flush(first) and is_flush(second):
            winner = winning_hand(first, second)
            if winner == first:
                player_one += 1
            else:
                player_two += 1
        elif is_flush(first):
            player_one += 1
        else:
            player_two += 1
    elif is_straight(first) or is_straight(second):
        if is_straight(first) and is_straight(second):
            winner = winning_hand(first, second)
            if winner == first:
                player_one += 1
            else:
                player_two += 1
        elif is_straight(first):
            player_one += 1
        else:
            player_two += 1
    elif is_three_of_a_kind(first) or is_three_of_a_kind(second):
        if is_three_of_a_kind(first) and is_three_of_a_kind(second):
            winner = winning_hand(first, second)
            if winner == first:
                player_one += 1
            else:
                player_two += 1
        elif is_three_of_a_kind(first):
            player_one += 1
        else:
            player_two += 1
    elif is_two_pairs(first) or is_two_pairs(second):
        if is_two_pairs(first) and is_two_pairs(second):
            winner = winning_hand(first, second)
            if winner == first:
                player_one += 1
            else:
                player_two += 1
        elif is_two_pairs(first):
            player_one += 1
        else:
            player_two += 1
    elif is_one_pair(first) or is_one_pair(second):
        if is_one_pair(first) and is_one_pair(second):
            winner = winning_hand(first, second)
            if winner == first:
                player_one += 1
            else:
                player_two += 1
        elif is_one_pair(first):
            player_one += 1
        else:
            player_two += 1
    else:
        winner = winning_hand(first, second)
        if winner == first:
            player_one += 1
        else:
            player_two += 1

print player_one, player_two