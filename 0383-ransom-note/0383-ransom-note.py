class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        dict1 = {}
        
        for i in range(len(magazine)):
            if magazine[i] in dict1:
                dict1[magazine[i]] += 1
            else:
                dict1[magazine[i]] = 1
        
        for i in ransomNote:
            if i in magazine and dict1[i] > 0:
                dict1[i] -= 1
            else:
                return False
        
        return True




        