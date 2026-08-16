class Solution(object):
    def countDigits(self, num):

        count = 0
        og = num
        working = num

        for i in range(len(str(og))):
            digit = working % 10

            if og % digit == 0 :
                count += 1  
            
            working //= 10
        
        return count