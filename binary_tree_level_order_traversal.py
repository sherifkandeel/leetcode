# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from Queue import *
class Solution(object):
    def levelOrderBottom(self, root):
        if root == None:
            return []
        q = Queue()
        nq = Queue()
        q.put(root)
        lvls = []
        lvl = []
        while not q.empty():
            n = q.get()
            lvl.append(n.val)
            if n.left != None:
                nq.put(n.left)
            if n.right != None:
                nq.put(n.right)
            
            if q.empty():
                lvls.append(lvl)
                lvl = []
                q = nq
                nq = Queue()
        lvls.reverse()
        return lvls
            
            
            
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
