class Solution(object):
    def addBinary(self, a, b):
        return str(bin(int(a,2)+int(b,2)))[2:]
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
