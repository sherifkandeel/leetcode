class Solution(object):
    def isPalindrome(self, s):
        s = list(s)
        for i in range(len(s)):
            if not s[i].isalnum():
                s[i] = ' '
        s = ''.join(s).replace(" ","")
        for i in range(len(s)/2):
            if s[i].lower() != s[len(s)-1-i].lower():
                return False
        return True
        
        """
        :type s: str
        :rtype: bool
        """
        
