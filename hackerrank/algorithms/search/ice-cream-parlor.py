def find_flavors(money, flavors, prices):
    for i in range(flavors):
        for j in range(flavors):
            if i < j and (prices[i] + prices[j] == money):
                print str(i + 1) + " " + str(j + 1)

test_cases = int(raw_input())

for case in range(test_cases):
    money = int(raw_input())
    flavors = int(raw_input())
    prices = [int(x) for x in raw_input().split()]
    find_flavors(money, flavors, prices)