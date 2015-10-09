class Solution(object):
    def majorityElement(self, nums):
        count = 1
        majidx = 0
        for i in range(len(nums)):
            if nums[majidx] == nums[i]:
                count+=1
            else:
                count -= 1
            if count == 0:
                majidx = i
                count = 1
        return nums[majidx]
                    
        
        
    def majorityElement2(self, nums):
        d = {}
        maxidx = nums[0]
        for i in nums:
            if i in d:
                d[i] += 1
                if d[i] > d[maxidx]:
                    maxidx = i
            else:
                d[i] = 1
        return maxidx
            
                    
        
