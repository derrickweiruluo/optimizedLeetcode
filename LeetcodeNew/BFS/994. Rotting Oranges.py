"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.


##### Image:
https://leetcode.com/problems/rotting-oranges/

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.

"""
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        queue = collections.deque()
        time = 0
        fresh_count = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh_count += 1
                if grid[i][j] == 2:
                    queue.append((i, j))
                    
        dirs = [(1,0), (-1, 0), (0,1), (0, -1)]
        
        while queue and fresh_count:
            # while的下一个循环都是下一层，depth + 1， 这里对应的是时间+1
            time += 1
            for _ in range(len(queue)): # pop掉当前层的所有元素， 去感染下一层的新鲜桔子
                x, y = queue.popleft()
                for dx, dy in dirs:
                    xi, yi = x + dx, y + dy
                    if 0 <= xi < len(grid) and 0 <= yi < len(grid[0]):
                        # update 和 append下一层的元素
                        if grid[xi][yi] == 1:
                            fresh_count -=1
                            grid[xi][yi] = 2
                            queue.append((xi, yi))
        
        return time if not fresh_count else -1
