class Solution(object):
    def twoSum(self, nums, target):
        
        dict1 = {}

        for i in range(len(nums)):
            curr = nums[i]
            reqd = target - curr

            if reqd in dict1:
                return (dict1[reqd], i)

            else:
                dict1[curr] = i
        