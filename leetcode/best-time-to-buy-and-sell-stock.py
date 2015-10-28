class Solution(object):
    def maxProfit(self, prices):
        if len(prices) < 2: return 0
        low, profit = prices[0], 0
        for i in range(1, len(prices)):
            if prices[i] < low:
                low = prices[i]
            if prices[i] - low > profit:
                profit = prices[i] - low
        return profit