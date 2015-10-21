class Solution(object):
    def reverse(self, n, start, end):
        if start >= end:
            return
        while start < end:
            temp = n[start]
            n[start] = n[end]
            n[end] = temp
            start += 1
            end -= 1
    
    def rotate(self, nums, k):
        k %= len(nums)
        if k>0:
            self.reverse(nums, 0, len(nums)-1)
            self.reverse(nums, 0, k-1)
            self.reverse(nums, k, len(nums)-1)
           
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
