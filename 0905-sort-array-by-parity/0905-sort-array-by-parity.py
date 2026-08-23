class Solution(object):
    def sortArrayByParity(self, nums):

        start = 0
        length = len(nums)

        for i in range (0, length):
            if nums[i] % 2 == 0:
                nums[start] , nums[i] = nums[i], nums[start]
                start+=1

        return nums
        

        