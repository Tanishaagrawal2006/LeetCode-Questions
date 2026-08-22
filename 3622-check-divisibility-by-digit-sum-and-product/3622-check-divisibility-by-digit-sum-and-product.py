class Solution(object):
    def checkDivisibility(self, n):

        sum = 0
        product = 1
        num = n

        while num > 0:

            digit = num % 10    
            sum += digit
            product *= digit
            num /= 10
    
        return n%(sum + product) == 0
        

            

            
             