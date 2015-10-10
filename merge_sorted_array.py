class Solution(object):
    def merge(self, nums1, m, nums2, n):
        k = m + n -1
        i1 = m - 1
        i2 = n - 1
        while k>=0:
            if i2<0 or (i1 >=0 and nums1[i1] >= nums2[i2]):
                nums1[k] = nums1[i1]
                i1 -= 1
            else:
                nums1[k] = nums2[i2]
                i2 -= 1
            k -= 1
        
                
                
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        
