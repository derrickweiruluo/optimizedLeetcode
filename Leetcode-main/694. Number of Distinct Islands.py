class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        
        row, col = len(grid), len(grid[0])
        uniqueIsland = set([])
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    uniqueIsland.add(self.dfs(grid, i, j, "start"))
        
        return len(uniqueIsland)
    
    def dfs(self, grid, i, j, path):
        if i < 0 or i > len(grid) - 1 or j < 0 or j > len(grid[0]) - 1 or grid[i][j] == 0:
            return ""
        
        grid[i][j] = 0
        
        return path \
                + self.dfs(grid, i - 1, j, "u") + "d" \
                + self.dfs(grid, i + 1, j, "d") + "u" \
                + self.dfs(grid, i, j - 1, "l") + "r" \
                + self.dfs(grid, i, j + 1, "r") + "l"
