class Solution(object):
    def islandPerimeter(self, grid):
        pr = 0
        if len(grid) == 0:
            return 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    if i - 1 == -1 or grid[i - 1][j] == 0:
                        pr += 1
                    if i + 1 == len(grid) or grid[i + 1][j] == 0:
                        pr += 1
                    if j - 1 == -1 or grid[i][j - 1] == 0:
                        pr += 1
                    if j + 1 == len(grid[i]) or grid[i][j + 1] == 0:
                        pr += 1
        return pr


