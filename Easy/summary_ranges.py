class Solution(object):
    def summaryRanges(self, nums):
        if len(nums) == 0:
            return []
        start = nums[0]
        summarylist = []
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1] +1:
                if nums[i-1] == start:
                    summarylist.append(str(start))
                else:
                    summarylist.append(str(start)+"->"+str(nums[i-1]))
                start = nums[i]
        if nums[-1] == start:
            summarylist.append(str(start))
        else:
            summarylist.append(str(start)+"->"+str(nums[-1]))
        return summarylist
                
            
            
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        
