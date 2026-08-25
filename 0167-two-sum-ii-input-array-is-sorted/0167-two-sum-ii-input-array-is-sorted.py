class Solution(object):
    def twoSum(self, numbers, target):
        
        left = 0
        right = len(numbers) - 1 

        while left < right:
            sum1 = numbers[right] + numbers[left]

            if sum1 == target :
                return [left+1, right+1]
            elif sum1 > target:
                right -=1
            else:
                left +=1
            
        



        
        

        