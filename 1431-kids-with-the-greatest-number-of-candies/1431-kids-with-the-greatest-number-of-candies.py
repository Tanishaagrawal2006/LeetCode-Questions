class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        
        ans = []
        max_candies = max(candies)

        for i in candies:
            ans.append(i + extraCandies >= max_candies)

        return [(i + extraCandies >= max_candies) for i in candies]