class Solution(object):
    def plusOne(self, digits):
        return map(int, list(str(int(''.join(map(str,digits))) + 1)))

        """
        2,3 -> 2,4
        0 -> 1
        20 -> 1
        29 -> 30
        2999 -> 3000
        999 -> 1000
        :type digits: List[int]
        :rtype: List[int]
        """
        
