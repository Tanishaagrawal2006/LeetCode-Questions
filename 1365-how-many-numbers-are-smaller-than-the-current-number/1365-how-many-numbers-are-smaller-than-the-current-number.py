class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        
        arr = []

        for i in nums:

            count = 0

            for j in nums:
                if i > j :
                    count+= 1   

            arr.append(count)

        return arr