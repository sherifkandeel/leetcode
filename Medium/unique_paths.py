class Solution(object):
    
    # a solution that involves recursion and backtracking but this will exceed time limit
    # def dfs(self, col, row, targetrow, targetcol):
    #     if col+row > targetrow+targetcol:
    #         return 0
    #     if col == targetcol and row == targetrow:
    #         return 1
    #     if col> targetcol or row> targetrow:
    #         return 0
    #     paths = self.dfs(col+1, row, targetrow, targetcol)
    #     paths += self.dfs(col, row+1, targetrow, targetcol)
    #     return paths
        
    # solution involving finding factorial with memoization to ensure faster solution time
    def __init__(self):
        self.fdict = {}
    def f(self, num):
        if num == 0:
            return 1
        if num in self.fdict:
            return self.fdict[num]
        else:
            self.fdict[num] = num*self.f(num-1)
            return self.fdict[num]
    
    def uniquePaths(self, m, n):
        #because eventually it is a choose m+n from a set of two
        return self.f(m+n-2)/(self.f(n-1)*self.f(m-1))
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
