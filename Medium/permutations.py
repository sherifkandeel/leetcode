class Solution(object):
    def permute(self, nums):
        if len(nums) == 1:
            return [nums]
        results = []
        for i in range(len(nums)):
            nums[0], nums[i] = nums[i], nums[0]
            tempres = self.permute(nums[1:])
            for ar in tempres:
                results.append([nums[0]]+ar)
        return results
            
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
