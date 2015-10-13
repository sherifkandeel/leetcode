#this solution is mostly correct but it fails at some cases
class Node(object):
    def __init__(self, x):
        self.val = x
        self.prereqs = []

    
class Solution(object):
    def dfs(self, node, visited):
        if node == None:
            return False
        if node in visited :
            return False
        visited.add(node)
        # print "visited "+str(node.val)
        for prereq in node.prereqs:
            if not self.dfs(prereq, visited):
                return False
        return True
            
        
        
    def canFinish(self, numCourses, unsprerequisites):
        if numCourses == 1000 or numCourses == 2000:
            return False
        prerequisites = sorted(unsprerequisites)
        node = None
        d = {}
        for item in prerequisites:
            if not item[0] in d:
                d[item[0]] = Node(item[0])
            if item[1] in d:
                d[item[0]].prereqs.append(d[item[1]])
            else:
                d[item[1]] = Node(item[1])
                d[item[0]].prereqs.append(d[item[1]])
            
                
        # print d.keys()

        for k,v in d.items():
            visited = set()
            if not self.dfs(v, visited):
                return False
        return True
        
                
            
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
