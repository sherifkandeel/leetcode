# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from Queue import *
class Solution(object):
    def levelOrder(self, root):
        if root == None:
            return []
        q = Queue()
        new_q = Queue()
        lvl = []
        lvls = []
        q.put(root)
        while not q.empty():
            item = q.get()
            if item.left !=None:
                new_q.put(item.left)
            if item.right != None:
                new_q.put(item.right)
            lvl.append(item.val)
            if q.empty():
                lvls.append(lvl)
                lvl = []
                q = new_q
                new_q = Queue()
        return lvls
            
        
        
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
