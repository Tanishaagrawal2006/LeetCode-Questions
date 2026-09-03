class Solution(object):
    def wordPattern(self, pattern, s):

        mapping = {}
        reverse_mapping = {}
        
        words = s.split()

        if len(pattern) != len(words):
            return False
            
        for i in range(len(pattern)):
            if pattern[i] in mapping:
                if mapping[pattern[i]] != words[i]:
                    return False
            else:
                mapping[pattern[i]] = words[i]

            if words[i] in reverse_mapping:
                if reverse_mapping[words[i]] != pattern[i]:
                    return False
            else:
                reverse_mapping[words[i]] = pattern[i]
        
        return True

        
            

        