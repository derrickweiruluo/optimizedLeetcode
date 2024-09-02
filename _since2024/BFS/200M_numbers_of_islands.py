import collections


class Solution:  # BFS  2
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




# class Solution:   #BFS 1
#     def numIslands(self, grid: List[List[str]]) -> int:
        
#         res = 0
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j] == '1':
#                     grid[i][j] = '0'
#                     queue = collections.deque([(i, j)])
#                     while queue:
#                         x, y = queue.popleft()
#                         for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
#                             xi, yi = x + dx, y + dy
#                             if 0 <= xi < len(grid) and 0 <= yi < len(grid[0]) and grid[xi][yi] == '1':
#                                 grid[xi][yi] = '0'
#                                 queue.append((xi, yi))
                    
#                     res += 1
        
#         return res