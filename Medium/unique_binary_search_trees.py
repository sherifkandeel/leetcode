import math
class Solution(object):
    def numTrees(self, n):
        #there's also the right way of doing it thorugh dynamic programming, which i don't know yet
        return (math.factorial(2*n))/(math.factorial(n+1)*math.factorial(n))
        """
        :type n: int
        :rtype: int
        """
        
