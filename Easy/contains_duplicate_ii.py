class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                for c in d[nums[i]]:
                    if abs(c-i) <= k:
                        return True
                d[nums[i]].append(i)
            else:
                d[nums[i]] = [i]
        return False
            
        
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
