'''
An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.
'''


class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        uniqueIslands = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    uniqueIslands.add(self.dfs(grid, i, j, 'start'))
        
        return len(uniqueIslands)
    
    def dfs(self, grid, i, j, path):
        if i < 0 or i > len(grid) - 1 or j < 0 or j > len(grid[0]) - 1\
        or grid[i][j] == 0:
            return "" # 如果当前是海, 返回 empty string as that path
        grid[i][j] = 0
        
        left = self.dfs(grid, i, j - 1, 'l') + 'r'
        right = self.dfs(grid, i, j + 1, 'r') + 'l'
        up = self.dfs(grid, i - 1, j, 'u') + 'd'
        down = self.dfs(grid, i + 1, j, 'd') + 'p'
        
        return path + left + right + up + down
    
        # Note for path recording
        '''
        why do we need the extra + "u" , or + "d" etc. ?
        Doesn't path + dfs(,'u') take care of it ?

        Explain : :
        1 1 1 - Start+RRD       ---> Start + RL + ""R + ""D + DU   @ at the 1st layer
        1 0 0

        1 1 1 - Also Start+RRD  ---> Start + RL + ""R + ""D + ""U  @ at the 1st layer
        0 1 0

        To avoid it, we append direction we took irrespective of whether that location had 1 or not'''