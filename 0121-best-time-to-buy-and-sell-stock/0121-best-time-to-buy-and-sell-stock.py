class Solution(object):
    def maxProfit(self, prices):
        
        min_price = prices[0]
        profit = 0

        for i in range(1, len(prices)):

            if prices[i] < min_price:
                min_price = prices[i]

            curr_profit = prices[i] - min_price

            if curr_profit > profit:
                profit = curr_profit

            if curr_profit < 0:
                curr_profit = 0
        
        return profit


        