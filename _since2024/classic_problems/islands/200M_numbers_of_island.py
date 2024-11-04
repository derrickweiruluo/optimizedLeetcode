import collections


class Solution:  # BFS_2
    def numIslands(self, grid: List[List[str]]) -> int:

        def bfs(grid, i, j):
            grid[i][j] = "2"
            queue = collections.deque([(i, j)])
            while queue:
                x, y = queue.popleft()
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    x1, y1 = x + dx, y + dy
                    if 0 <= x1 < len(grid) and 0 <= y1 < len(grid[0]) and grid[x1][y1] == "1":
                        grid[x1][y1] = "2"
                        queue.append((x1, y1))
            return 1

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    res += bfs(grid, i, j)
        return res



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