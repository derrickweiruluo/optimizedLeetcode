# 问有且仅有两个岛屿的最短距离


# Clarificaitions:
# 有且仅有两个岛屿
# Garantee there is a path which means

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        
        boundOne = set()
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        m, n = len(grid), len(grid[0])
        steps = 0
        i, j = self.get_first(grid)
        self.dfs(grid, i, j, boundOne)
        queue = collections.deque(list(boundOne))
        
        while queue:
            steps += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in dirs:
                    xi, yi = x + dx, y + dy
                    if 0 <= xi < m and 0 <= yi < n:
                        if grid[xi][yi] == 1:
                            return steps
                        elif grid[xi][yi] == 0:
                            queue.append((xi, yi))
                            grid[xi][yi] = -1  # 沉默岛屿
        
        # print(boundOne)
    

    # get the cordinates of the first island
    def get_first(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return i, j
    
    # 一次性DFS方程来 收集第一个岛屿的周围的 "一圈水域" 的 coordinates
    def dfs(self, grid, i, j, boundOne):
        grid[i][j] = -1
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            xi, yi = i + dx, j + dy
            if 0 <= xi < len(grid) and 0 <= yi < len(grid[0]):
                if grid[xi][yi] == 0:
                    boundOne.add((xi, yi))
                elif grid[xi][yi] == 1:
                    self.dfs(grid, xi, yi, boundOne)