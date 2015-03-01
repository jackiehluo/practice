def max_toys(prices, money):
    cost = 0
    answer = 0
    prices.sort()
    for price in prices:
        if (cost + price) < money:
            cost += price
            answer += 1
        else:
            break
    return answer

if __name__ == '__main__':
    n, k = map(int, raw_input().split())
    prices = map(int, raw_input().split())
    print max_toys(prices, k)
