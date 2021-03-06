
# Time O(M^2 * N^2), Space O(1)
# MN time to scan
# might keep crushing 3-candy, with all candies are gone


class Solution:
    def candyCrush(self, grid: List[List[int]]) -> List[List[int]]:
        
        m, n = len(grid), len(grid[0])
        
        
        while True:
        #1 check
            crush = set()
            for i in range(m):
                for j in range(n):
                    if j > 1 and grid[i][j] and grid[i][j] == grid[i][j - 1] == grid[i][j - 2]:
                        crush |= {(i, j), (i, j - 1), (i, j - 2)}
                    if i > 1 and grid[i][j] and grid[i][j] == grid[i - 1][j] == grid[i - 2][j]:
                        crush |= {(i, j), (i - 1, j), (i - 2, j)}
            
            # 2, Crush
            if not crush: break
            for i, j in crush: 
                grid[i][j] = 0

            # 3, Drop
            for j in range(n):
                bottom = m - 1
                # dropping the candice and move up the bottome for the cur column
                for i in range(m - 1, -1, -1):
                    if grid[i][j]: 
                        grid[bottom][j] = grid[i][j]
                        bottom -= 1
                
                # update everything above the bottom line to zeroes
                for i in range(bottom + 1): 
                    grid[i][j] = 0
                    
        return grid