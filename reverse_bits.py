class Solution(object):
    def reverseBits(self, n):
        return int('{:032b}'.format(n)[::-1], 2)
        """
        :type n: int
        :rtype: int
        """
        
