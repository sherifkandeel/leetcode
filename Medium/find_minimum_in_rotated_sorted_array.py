class Solution(object):
    def findMin(self, nums):
        for i in range(len(nums)):
            if i == 0: continue
            if nums[i] < nums[i-1]:
                return nums[i]
        return nums[0]
            
             
        """
        :type nums: List[int]
        :rtype: int
        """
        
