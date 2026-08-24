class Solution(object):
    def lengthOfLastWord(self, s):
        
        count = 0
        s = s.strip()
        right = len(s) - 1

        while right >= 0 and s[right] != " ":
            count +=1
            right -=1

        return count

        

        



        