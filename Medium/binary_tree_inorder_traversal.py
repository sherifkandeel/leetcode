# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        if root == None:
            return []
        inorderlist = []
        inorderlist.extend(self.inorderTraversal(root.left))
        inorderlist.append(root.val)
        inorderlist.extend(self.inorderTraversal(root.right))
        return inorderlist
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
