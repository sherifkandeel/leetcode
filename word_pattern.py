class Solution(object):
    def wordPattern(self, pattern, str):
        d = {}
        s = set()
        words = str.split(' ')
        p = list(pattern)
        if len(words) != len(p):
            return False
        for i in range(len(p)):
            if p[i] in d:
                if words[i] != d[p[i]]:
                    return False
            else:
                if words[i] in s:
                    return False
                s.add(words[i])
                d[p[i]] = words[i]
        return True
                
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        
