class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rotten = collections.deque()
        fresh_cnt = 0
        minPassed = 0
        
        row, col = len(grid), len(grid[0])
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    rotten.append((i, j))
                elif grid[i][j] == 1:
                    fresh_cnt += 1
                    
        while fresh_cnt > 0 and rotten:
            minPassed += 1
            for _ in range(len(rotten)):
                x, y = rotten.popleft()
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    xi , yi = x + dx, y + dy
                    if xi < 0 or xi > row - 1 or yi < 0 or yi > col - 1:
                        continue
                    if grid[xi][yi] == 0 or grid[xi][yi] == 2:
                        continue
                    
                    fresh_cnt -= 1
                    grid[xi][yi] = 2
                    rotten.append((xi, yi))
                    
        return minPassed if fresh_cnt == 0 else -1
