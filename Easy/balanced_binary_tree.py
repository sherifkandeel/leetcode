# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def get_depth(self, root):
        if root == None:
            return 0
        return max(self.get_depth(root.left)+1, self.get_depth(root.right)+1)
    def isBalanced(self, root):
        if root == None:
            return True
        
        maxleft = self.get_depth(root.left)
        maxright = self.get_depth(root.right)
        if abs(maxleft-maxright) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
        
        """
        :type root: TreeNode
        :rtype: bool
        """
        
