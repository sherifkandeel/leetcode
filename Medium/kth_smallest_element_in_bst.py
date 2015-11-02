# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorder(self, root, k):
        if root == None:
            return -1
        v1 = self.inorder(root.left, k)
        if v1 > -1: return v1
        k[0] -= 1
        if k[0] == 0:
            return root.val
        v2 = self.inorder(root.right, k)
        if v2 > -1: return v2
        return -1
    
    def kthSmallest(self, root, k):
        return self.inorder(root, [k])
    
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        
