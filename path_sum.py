# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, root, dsum , csum):
        if root == None:
            return False
        if root.left == None and root.right==None:
            if csum+root.val == dsum:
                return True
            else:
                return False
        left = self.dfs(root.left, dsum, csum+root.val)
        right = self.dfs(root.right, dsum, csum+root.val)
        if left or right:
            return True
        return False
    
    
    def hasPathSum(self, root, sum):
        return self.dfs(root, sum, 0)
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
       
