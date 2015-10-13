class Solution(object):
    def isIsomorphic(self, s, t):
        vals = set()
        if len(s) != len(t):
            return False
        d = {}
        for i in range(len(s)):
            if s[i] in d:
                if t[i] != d[s[i]]:
                    return False
            elif t[i] not in vals:
                d[s[i]] = t[i]
                vals.add(t[i])
            else:
                return False
        return True
        
        """
        
        :type s: str
        :type t: str
        :rtype: bool
        """
        
