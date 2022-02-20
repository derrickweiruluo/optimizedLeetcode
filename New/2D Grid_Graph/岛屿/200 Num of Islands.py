from collections import deque

# DFS, time O(M * N), Space O(M * N) worse case when it is full of land
class Solution:  
    def numIslands(self, grid: List[List[str]]) -> int:
        
        res = 0
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def dfs(grid, x, y):
            grid[x][y] = '-1'
            for dx, dy in dirs:
                xi, yi = x + dx, y + dy
                if 0 <= xi < m and 0 <= yi < n and grid[xi][yi] == '1':
                    dfs(grid, xi, yi)
        
        
        
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(grid, i, j)
                    res += 1
        
        return res



# time O(M * N), Space O(min(M,N)) worse case when it is full of land
# because in worst case where the grid is filled with lands, the size of queue can grow up to min(M,N)
class Solution:  # BFS  
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    grid[i][j] = '0'
                    self.bfs(grid, i, j)
                    res += 1
        return res
    
    def bfs(self, grid, i, j):
        queue = collections.deque([(i,j)])
        while queue:
            x, y = queue.popleft()
            for dx, dy in [(1,0), (-1,0), (0,1), (0, -1)]:
                xi, yi = x + dx, y + dy
                if 0 <= xi < len(grid) and 0 <= yi < len(grid[0]) and grid[xi][yi] == '1':
                    grid[xi][yi] = '0'
                    queue.append((xi, yi))



class Solution:  # Same BFS
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    grid[i][j] = '0'
                    queue = collections.deque([(i,j)])
                    while queue:
                        x, y = queue.popleft()
                        for dx, dy in [(1,0), (-1,0), (0,1), (0, -1)]:
                            xi, yi = x + dx, y + dy
                            if 0 <= xi < len(grid) and 0 <= yi < len(grid[0]) and grid[xi][yi] == '1':
                                grid[xi][yi] = '0'
                                queue.append((xi, yi))
                    res += 1
        return res