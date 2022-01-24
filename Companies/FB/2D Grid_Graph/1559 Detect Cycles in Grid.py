

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        
        m , n = len(grid), len(grid[0])
        visited = set()
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def dfs(i, j, prev, seen):
            # print((i, j))  # at most visited the whole graph
            
            
            # 如果绕一圈可以回到一个访问过的点，就是有circle
            if (i, j) in seen: 
                return True

            seen.add((i, j))
            visited.add((i, j))
            for dx, dy in dirs:
                xi, yi = i + dx, j + dy
                if 0 <= xi < m and 0 <= yi < n and grid[xi][yi] == grid[i][j]: # same color
                    if not prev or prev != (xi, yi):                           # just dont go backward by checking != prev
                        if dfs(xi, yi, (i, j), seen):
                            return True
            return False
        
        
        for i in range(m):
            for j in range(n):
                if (i, j) not in visited:
                    seen = set()
                    if dfs(i, j, None, seen):   # each segregated island has a set() to start
                        return True
        
        return False