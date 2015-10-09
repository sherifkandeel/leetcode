import math
class Solution(object):
    def isPowerOfTwo(self, n):
        if n <0:
            return False
        if n == 0:
            return False
        num = math.log(n,2)
        if round(num,10) == int(num):
            return True
        return False
        
