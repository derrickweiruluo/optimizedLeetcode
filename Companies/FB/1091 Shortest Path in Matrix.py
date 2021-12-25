'''
A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:
从左上到右下角的最短距离

'''

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        if grid[0][0] == 1 or grid[-1][-1] == 1: return -1
        
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1),  (-1, -1), (-1, 1)]
        m, n = len(grid), len(grid[0])
        
        visited = set()
        visited.add((0, 0))
        
        queue = collections.deque([(0, 0, 1)])
        
        while queue:
            x, y, dist = queue.popleft()
            if x == m - 1 and y == n - 1:
                return dist
            for dx, dy in dirs:
                xi, yi = x + dx, y + dy
                if 0 <= xi < m  and 0 <= yi < n and grid[xi][yi] == 0 and (xi, yi) not in visited:
                    visited.add((xi, yi))
                    queue.append((xi, yi, dist + 1))
        
        return -1