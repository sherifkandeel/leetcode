# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def insert(self, root, num):
        if root.val > num:
            if root.left == None:
                root.left = TreeNode(num)
                return
            else:
                self.insert(root.left, num)
        if root.val < num:
            if root.right == None:
                root.right = TreeNode(num)
                return
            else:
                self.insert(root.right, num)
                
                
    def bs(self, nums, outarr):
        if len(nums) == 0: 
            return
        mid = len(nums)/2
        outarr.append(nums[mid])
        self.bs(nums[:mid], outarr)
        self.bs(nums[mid+1:], outarr)
    
    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        outarr = []
        self.bs(nums, outarr)
        root = TreeNode(-1)
        for i in range(len(outarr)):
            if i==0:
                root.val = outarr[i]
            self.insert(root, outarr[i])
        return root
                
        print outarr
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
