class Solution(object):
    def missingNumber(self, nums):
        nums.extend([-1])
        for i in range(len(nums)):
            while i!= nums[i] and nums[i] !=-1:
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        
        for i in range(len(nums)):
            if nums[i] == -1:
                return i
        """
        :type nums: List[int]
        :rtype: int
        """
        
