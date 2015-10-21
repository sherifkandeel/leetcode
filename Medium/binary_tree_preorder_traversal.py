# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        if root == None:
            return []
        prelist = [root.val]
        prelist.extend(self.preorderTraversal(root.left))
        prelist.extend(self.preorderTraversal(root.right))
        return prelist
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
