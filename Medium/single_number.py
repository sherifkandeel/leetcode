class Solution(object):
    def singleNumber(self, nums):
        x = 0 
        for num in nums:
            x = x ^ num
        return x
        
        """
        :type nums: List[int]
        :rtype: int
        """
        
