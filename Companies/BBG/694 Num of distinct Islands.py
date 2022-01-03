'''
不同形状的岛屿的树木
'''


class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        uniqueIslands = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    uniqueIslands.add(self.dfs(grid, i, j, m, n, 'start'))
        return len(uniqueIslands)
    
    def dfs(self, grid, i, j, m, n, path):
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
            return ''
        grid[i][j] = 0
        
        left = self.dfs(grid, i, j - 1, m, n, 'l') + 'r'
        right = self.dfs(grid, i, j + 1, m, n, 'r') + 'l'
        up = self.dfs(grid, i - 1, j, m, n, 'u') + 'd'
        down = self.dfs(grid, i + 1, j, m, n, 'd') + 'u'
        return path + left + right + up + down
        
        # Note for path recording
        '''
        why do we need the extra + "u" , or + "d" etc. ?
        Doesn't path + dfs(,'u') take care of it ?

        Explain : :
        1 1 1 - SRRD
        1 0 0

        1 1 1 - Also SRRD
        0 1 0

        To avoid it, we append direction we took irrespective of whether that location had 1 or not'''