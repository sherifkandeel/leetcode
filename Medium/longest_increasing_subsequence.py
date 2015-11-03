class Solution(object):
    def lengthOfLIS(self, nums):
        if len(nums) <=1:
            return len(nums)
        dp = [1 for i in nums]
        
        for i in range(1,len(nums)):
            maxx = 0
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j] > maxx:
                        maxx = dp[j]
            dp[i] = maxx + 1
        # print dp
        return max(dp)
                
        
        
        """
        :type nums: List[int]
        :rtype: int
        """
        
