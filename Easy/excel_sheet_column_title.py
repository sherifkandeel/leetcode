class Solution(object):
    def convertToTitle(self, n):
        col = ''
        while n>0:
            current = n%26
            if current == 0:
                n-=1
                col+='z'
            else:
                col+=chr(96+current)
            n /= 26
        col = col[::-1]
        return col.upper()
            
        
        """
        :type n: int
        :rtype: str
        """
        
