class Solution(object):
    def reverse(self, x):
        isnegative = False
        if x == 0:
            return 0
        if x<0:
            isnegative = True
            x*=-1
        res = 0
        ln = len(str(x))
        while ln > 0:
            t = x%10
            t*= 10**(ln-1)
            res += t
            ln -= 1
            x /= 10
        #a fucken hack because python is too damn cool and doesn't give a shit about your overflow test case
        if res > 2147483647:
            return 0
        if isnegative:
            res*=-1
        return res
        """
        :type x: int
        :rtype: int
        """
        
