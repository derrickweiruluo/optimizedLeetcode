# 格子traversal基操

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        
        queue = collections.deque([(0, 0, 1)])
        visited = set()
        visited.add((0, 0))
        dirs = [(1, 0), (1, -1), (1, 1), (-1, 0), (-1, -1), (-1, 1), (0, -1), (0, 1)]
        n = len(grid)
                
        while queue:
            x, y, dist = queue.popleft()
            
            if x == n - 1 and y == n - 1:
                return dist
            
            for dx, dy in dirs:
                xi, yi = x + dx, y + dy
                if 0 <= xi < n and 0 <= yi < n and grid[xi][yi] == 0 and (xi, yi) not in visited:
                    queue.append((xi, yi, dist + 1))
                    visited.add((xi, yi))
            
        
        return - 1
