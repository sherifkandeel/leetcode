class Solution(object):
    def productExceptSelf(self, nums):
        result = [1 for i in nums]
        for i in range(len(nums)-1):
            result[i+1] = nums[i]*result[i]
        
        result2 = [1 for i in nums]
        for i in range(len(nums)-1, 0,-1):
            result2[i-1] = result2[i]*nums[i]
        return [a*b for a,b in zip(result, result2)]
            
        
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
