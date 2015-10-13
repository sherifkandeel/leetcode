class Solution(object):
    def lengthOfLastWord(self, s):
        return len(s.strip().split(' ')[-1])
        """
        :type s: str
        :rtype: int
        """
        
