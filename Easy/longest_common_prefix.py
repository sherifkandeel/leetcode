class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        strs.sort(key = lambda s: len(s))
        base = strs[0]
        for i in range(len(base)):
            for j in range(len(strs)):
                if strs[j][i] != base[i]:
                    return base[0:i]
        return base
        
        """
        :type strs: List[str]
        :rtype: str
        """
        
