def count_cards(cards, i):
    count = 0
    for j in range(len(cards)):
        if cards[j] <= i:
            count += 1
    return count
            
test_cases = int(raw_input())

for case in range(test_cases):
    size = int(raw_input())
    cards = [int(x) for x in raw_input().split()]
    total_ways = 1
    for i in range(len(cards)):
        ways = max(0, count_cards(cards, i) - i)
        total_ways *= ways
    print total_ways