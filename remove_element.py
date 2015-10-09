class Solution(object):
    def removeElement(self, nums, val):
        new_length = len(nums)
        i = 0
        while i < new_length:
            if nums[i] == val:
                nums[i], nums[new_length-1] = nums[new_length-1], nums[i]
                new_length -= 1
            else:
                i += 1
        return new_length
            
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
