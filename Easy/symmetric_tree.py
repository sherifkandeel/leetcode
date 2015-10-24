# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    #solution that involves printing the inorder traversal and checking if it's palindrome
    # def inorder(self, root, vlist):
    #     if root == None:
    #         return 
    #     if root.left == None and root.right != None:
    #         vlist.append(-1)
    #     else:
    #         self.inorder(root.left, vlist)
    #     vlist.append(root.val)
    #     if root.right == None and root.left != None:
    #         vlist.append(-1)
    #     else:
    #         self.inorder(root.right, vlist)
    #     return
    #  def isSymmetric(self, root):
    #     vlist = []
    #     self.inorder(root, vlist)
    #     for i in range(len(vlist)/2):
    #         if vlist[i] != vlist[-(i+1)]:
    #             return False
    #     return True
    
    # A simple recursive solution DFS 
    def sym(self, left, right):
        if left == None and right == None: return True
        elif left == None or right == None: return False
        if left.val != right.val:
            return False
        return self.sym(left.left, right.right) and self.sym(left.right, right.left)
        
    def isSymmetric(self, root):
        if root == None: return True
        return self.sym(root.left, root.right)   
        
        
        """
        :type root: TreeNode
        :rtype: bool
        """
        
