class Solution(object):
    def myAtoi(self, str):
        maxint = 2147483647
        minint = -2147483648
        str = str.strip()
        if str == None or str=='':
            return 0
        
        isNegative = False
        start = 0
        if str[0] == '-':
            isNegative = True
            start = 1
        elif str[0] == '+':
            start = 1
        result = 0
        for i in range(start, len(str)):
            if str[i] < '0' or str[i] > '9':
                break
            result = result*10 + (ord(str[i]) - ord('0'))
        
        
        if isNegative:
            result *=-1
            
        if result >= maxint:
            return maxint
        elif result <= minint:
            return minint
        
        return result
            
        
        
        
        
        
        """
        :type str: str
        :rtype: int
        """
        
