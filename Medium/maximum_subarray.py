class Solution(object):
    def maxSubArray(self, nums):
        dp = [0 for x in nums]
        for i in range(len(nums)):
            if i==0:
                dp[i] = nums[i]
            elif nums[i] > nums[i] + dp[i-1]:
                dp[i] = nums[i] 
            else:
                dp[i] = nums[i] + dp[i-1]
        return max(dp)
            
        
        
        """
        [−2,1,−3,4,−1,2,1,−5,4]
        [-2, -1, -4, 0, -1, 1, 3, -2, 2]
        [
        :type nums: List[int]
        :rtype: int
        """
        
