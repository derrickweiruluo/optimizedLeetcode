class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        
        boundOne = set()  # to store boundary of the first found island
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rows, cols = len(grid), len(grid[0])
        
        def get_first():
            for i in range(rows):
                for j in range(cols):
                    if grid[i][j] == 1:
                        return (i, j)
        
        def dfs(i, j):  # to complete the boundary of the first island found above
            grid[i][j] = -1  # not dfs if mark as -1
            for dx, dy in dirs:
                xi, yi = i + dx, j + dy
                if 0 <= xi < rows and 0 <= yi < cols:
                    if grid[xi][yi] == 0:
                        boundOne.add((i, j))
                    elif grid[xi][yi] == 1:
                        dfs(xi, yi)
        
        steps = 0
        i, j = get_first(grid)
        dfs(grid, i, j)
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
                            grid[xi][yi] = -1
        
        return steps
