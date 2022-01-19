

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        fresh_count = 0
        queue = collections.deque()
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        step = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:     # fresh
                    fresh_count += 1
                if grid[i][j] == 2:     # rotted
                    queue.append((i, j))
        
        while queue and fresh_count:
            step += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in dirs:
                    xi, yi = x + dx, y + dy
                    if 0 <= xi < len(grid) and 0 <= yi < len(grid[0]):
                        if grid[xi][yi] == 1:  # next fresh to be rotted
                            fresh_count -= 1
                            grid[xi][yi] = 2
                            queue.append((xi, yi))
        
        return step if not fresh_count else -1


class Solution3: # just pyhtonic
    def orangesRotting(self, grid):
        bfs, t, m, n = [(i, j) for i, row in enumerate(grid) for j, val in enumerate(row) if val == 2], 0, len(grid), len(grid[0])
        while bfs:
            new = []
            for i, j in bfs:
                for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                        grid[x][y] = 2
                        new.append((x, y))
            bfs = new
            t += bool(bfs)
        return t if all(val != 1 for row in grid for val in row) else -1