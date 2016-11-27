class Solution(object):
    def intersect(self, nums1, nums2):
        ls1 = sorted(nums1)
        ls2 = sorted(nums2)
        intersection = [] 
        i, j = 0, 0
        while i < len(ls1) and j < len(ls2):
            if ls1[i] == ls2[j]:
                intersection.append(ls1[i])
                i += 1
                j += 1
            elif ls1[i] > ls2[j]:
                j += 1
            elif ls1[i] < ls2[j]:
                i += 1
        return intersection


        
