class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) <= 1:
            return len(nums)
        i = 1
        j = 1
        while i < len(nums):
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j += 1
            i += 1
        return j
        
        """
        :type nums: List[int]
        :rtype: int
        """
        
