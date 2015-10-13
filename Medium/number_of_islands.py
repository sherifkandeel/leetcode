class Solution(object):
    def dfs(self, row, col, grid, visited):
        if row <0 or row >= len(grid) or col <0 or col >= len(grid[0]):
            return
        if visited[row][col]:
            return
        if grid[row][col] == '0':
            return
        visited[row][col] = True
        self.dfs(row, col+1, grid, visited)
        self.dfs(row, col-1, grid, visited)
        self.dfs(row+1, col, grid, visited)
        self.dfs(row-1, col, grid, visited)
            
    

    def numIslands(self, grid):
        if len(grid) == 0:
            return 0
        visited = [[False for x in range(len(grid[0]))] for y in range(len(grid))]
        islands_count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1' and not visited[row][col]:
                    islands_count += 1
                    self.dfs(row, col, grid, visited)
        return islands_count
                
            
        
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
