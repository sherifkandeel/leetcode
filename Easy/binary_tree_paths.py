# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

b = sorted(d.values())
class Solution(object):
    def dfs (self, root, path, paths):
        # global paths
        if root.right == None and root.left == None:
            b = path+[root.val]
            paths.append('->'.join(map(str, b)))
        if root.left != None:
            self.dfs(root.left, path+[root.val], paths)
        if root.right != None:
            self.dfs(root.right, path+[root.val], paths)
            
    def binaryTreePaths(self, root):
        # global paths
        if root == None:
            return []
        paths = []
        self.dfs(root,[], paths)
        return paths
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        
