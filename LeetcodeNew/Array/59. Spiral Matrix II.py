# https://leetcode.com/problems/spiral-matrix-ii/discuss/22282/4-9-lines-Python-solutions
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        nums = [x for x in range(n * n)]
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        grid = [[0] * n for _ in range(n)]
        i = j = 0
        idx = 0
        
        
        dx, dy = 0, 1
        for k in range(n * n):
            grid[i][j] = k + 1
            if grid[(i + dx) % n][(j + dy) % n]:
                dx, dy = dy, -dx
            i += dx
            j += dy
        
        return grid