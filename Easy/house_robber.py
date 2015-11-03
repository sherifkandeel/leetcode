class Solution(object):
    def rob(self, nums):
        if len(nums) == 0:
            return 0
        if len(nums) == 2:
            return max(nums)
        #we are adding a zero ahead in the array to make logic work for all cases
        dp = [0 for i in range(len(nums)+1)]
        for i in range(len(nums)):
            if i < 1:
                dp[i+1] = nums[i]
                continue
            if nums[i] + dp[i-1] > dp[i]:
                dp[i+1] = nums[i] + dp[i-1]
            else:
                dp[i+1] = dp[i]
        print dp
        return dp[len(dp)-1]
        """
        :type nums: List[int]
        :rtype: int
        """
        
