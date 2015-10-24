class Solution(object):
    def findPeakElement(self, nums):
        if len(nums) == 1:
            return 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                if i==0:
                    return i
                elif nums[i]> nums[i-1]:
                    return i
        return len(nums) -1
        """
        :type nums: List[int]
        :rtype: int
        """
        
