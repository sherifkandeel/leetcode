# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if root == None:
            return None
        if (p.val > root.val and q.val < root.val) or (q.val > root.val and p.val < root.val):
            return root
        elif p.val == root.val or q.val == root.val:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left != None:
            return left
        if right != None:
            return right
