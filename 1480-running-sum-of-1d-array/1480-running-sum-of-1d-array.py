class Solution(object):
    def runningSum(self, nums):
        
        runningSum = []
        total = 0

        for i in range(len(nums)):
            total += nums[i]
            runningSum.append(total)
            
        return runningSum

        