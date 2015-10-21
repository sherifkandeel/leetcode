class Solution(object):
    def searchInsert(self, nums, target):
        if len(nums) == 0:
            return 0
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = start + (end-start)/2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid -1
            else:
                start = mid + 1
        return start
             
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
         
