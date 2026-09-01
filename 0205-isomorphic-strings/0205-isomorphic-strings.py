class Solution(object):
    def isIsomorphic(self, s, t):
        
        mapping = {}
        reverse_mapping = {}

        for i in range(len(s)):
            if s[i] in mapping:
                if mapping[s[i]] != t[i]:
                    return False
            else:
                mapping[s[i]] = t[i]
            
            if t[i] in reverse_mapping:
                if reverse_mapping[t[i]] != s[i]:
                    return False
            else:
                reverse_mapping[t[i]] = s[i]

        return True




        