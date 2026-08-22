class Solution(object):
    def removeDuplicates(self, nums):
        
        start = 2
        length = len(nums)

        if length <= 2:
            return length

        for i in range (2, length):
            if nums[i] != nums[start - 2]:
                start += 1
                nums[start - 1] = nums[i]
        
        return start

        

        