class Solution(object):
    def subtractProductAndSum(self, n):
        
        temp = n
        prod = 1
        sum = 0

        while temp > 0:
            rem = temp % 10
            temp //= 10

            sum += rem
            prod *= rem

        return prod - sum