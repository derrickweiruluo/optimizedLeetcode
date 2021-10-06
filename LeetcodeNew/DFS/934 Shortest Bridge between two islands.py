'''
In a given 2D binary array grid, there are two islands.  (An island is a 4-directionally connected group of 1s not connected to any other 1s.)
Now, we may change 0s to 1s so as to connect the two islands together to form 1 island.

Return the smallest number of 0s that must be flipped.  (It is guaranteed that the answer is at least 1.)
题意包含的隐晦条件：
1. 一个岛屿内只有 1 没有 0 (实心陆地)
2. flipped number = len of bridge

EX 1:
Input: grid = [[0,1],[1,0]]
Output: 1

EX 2:
Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2

EX 3:
Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1
'''

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        
        boundOne = set() # 第一个岛的“海洋”边界是set，因为搜索的途中 ”除重“
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        m, n = len(grid), len(grid[0])
        steps = 0
        i, j = self.get_first(grid)  # 得到第一个岛的第一个坐标，然后以此 DFS 来构建其边界
        self.dfs(grid, i, j, boundOne)
        queue = collections.deque(list(boundOne))  #根据第一个岛的 “海洋”边界，然后朝外BFS， 
        
        while queue:
            steps += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in dirs:
                    xi, yi = x + dx, y + dy
                    if 0 <= xi < m and 0 <= yi < n:
                        if grid[xi][yi] == 1:
                            return steps
                        elif grid[xi][yi] == 0:  # 搜索过的海洋要标记 -1 防止再次搜索 因为重复搜索只会 >= 之前的BFS距离
                            queue.append((xi, yi))
                            grid[xi][yi] = -1
        
        print(boundOne)
        return steps
    
    def get_first(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return i, j
    
    def dfs(self, grid, i, j, boundOne): # 只有 1 的坐标才会被搜索
        grid[i][j] = -1
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            xi, yi = i + dx, j + dy
            if 0 <= xi < len(grid) and 0 <= yi < len(grid[0]):
                if grid[xi][yi] == 0: # 更新海洋边界
                    boundOne.add((xi, yi))
                elif grid[xi][yi] == 1:  # 只有 1 的坐标才会被搜索
                    self.dfs(grid, xi, yi, boundOne)
                
        
        