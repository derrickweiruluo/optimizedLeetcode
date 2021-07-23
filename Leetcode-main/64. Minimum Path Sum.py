class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # row, col = len(grid), len(grid[0])
        
        # i, j = row - 1, col - 1
        
        res = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    continue
                elif i and j:
                    grid[i][j] += min(grid[i][j - 1], grid[i - 1][j])
                elif i == 0:
                    grid[i][j] += grid[i][j - 1]
                else:
                    grid[i][j] += grid[i - 1][j]
        
        
        return grid[-1][-1] 
