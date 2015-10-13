# Definition for a undirected graph node
# class UndirectedGraphNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []
from Queue import *
class Solution(object):
    def dfs (self, node, maps):
        if node in maps:
            return maps[node]
        nn = UndirectedGraphNode(node.label)
        maps[node] = nn
        for neighbor in node.neighbors:
            maps[node].neighbors.append(self.dfs(neighbor, maps))
        return nn
            
    def cloneGraph(self, node):
        if node == None:
            return None
        return self.dfs (node, {})
        
                
        
        
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        
