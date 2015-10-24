class Solution(object):
    def __init__(self):
        self.mini = 9999
        
    #The solution that takes forever
    def dfs(self, grid, row, col, cost):
        if row>= len(grid) or col >= len(grid[0]):
            return
        
        if row == len(grid)-1 and col == len(grid)-1:
            if cost < self.mini:
                self.mini = cost 
        
        if cost > self.mini:
            return
        
        self.dfs(grid, row+1, col, cost+grid[row][col])
        self.dfs(grid, row, col+1, cost+grid[row][col])
        
    #The dp solution
    def dp(self, grid):
        dp = [[0 for y in range(len(grid[0]))] for x in range(len(grid))]
        for i in range(len(grid[0])):
            if i == 0:
                dp[0][i] = grid[0][i]
            else:    
                dp[0][i] = dp[0][i-1] + grid[0][i]
        
        for i in range(len(grid)):
            if i == 0:
                continue
            dp[i][0] = dp[i-1][0] + grid[i][0]
        
        for i in range(1,len(grid)):
            for j in range(1,len(grid[0])):
                if dp[i-1][j] < dp[i][j-1]:
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                else:
                    dp[i][j] = dp[i][j-1] + grid[i][j]
        print dp
        return dp[-1][-1]
                
        
        
    
    
    def minPathSum(self, grid):
        # self.dfs(grid, 0,0,0)
        # return self.mini
        return self.dp(grid)
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
