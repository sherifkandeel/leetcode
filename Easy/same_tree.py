# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        if p == None and q == None:
            return True
        if p == None:
            return False
        if q == None:
            return False
        if p.val != q.val:
            return False
        left = isSameTree(p.left, q.left)
        right = isSameTree(p.right, q.right)
        if left == False or right == False:
            return False
        return True
        
        
        
        
