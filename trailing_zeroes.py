class Solution(object):
    def trailingZeroes(self, n):
        if n < 0:
            return -1
        count = 0
        i = 5
        while (n/i) >= 1:
            count += n / i
            i *= 5
        return count
        """
        :type n: int
        :rtype: int
        """
        
