class Solution(object):
    def maxProfit(self, prices):

        min_price = prices[0]
        profit = 0
        
        for i in range(1, len(prices)):

            if prices[i] < min_price:
                min_price = prices[i]

            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]

        return profit

        
        
        
        