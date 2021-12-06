'''
Solution Explanation

Because we are trying to find the shortest path, use BFS here to exit immediately when a path reaches the bottom right most cell.
Use a set to keep track of already visited paths. We only need to keep track of the row, column, and the eliminate obstacle usage count. We don't need to keep track of the steps because remember we are using BFS for the shortest path. That means there is no value storing a 4th piece of the data, the current steps. This will reduce the amount of repeat work.
m = rows
n = columns
k = allowed elimination usages

'''

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        queue = collections.deque([(0, 0, 0, 0)]) # i, j, obstacles, path
        m, n = len(grid), len(grid[0])
        if m == 1 and n == 1: return 0
        
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()
        
        while queue:
            x, y, cnt, path = queue.popleft()
            for dx, dy in dirs:
                xi, yi = x + dx, y + dy
                if 0 <= xi < m and 0 <= yi < n:
                    if grid[xi][yi] == 1 and cnt < k and (xi, yi, cnt + 1) not in visited:
                        visited.add((xi, yi, cnt + 1))
                        queue.append((xi, yi, cnt + 1, path + 1))
                    if grid[xi][yi] == 0 and (xi, yi, cnt) not in visited:
                        if xi == m - 1 and yi == n - 1:
                            return path + 1
                        visited.add((xi, yi, cnt))
                        queue.append((xi, yi, cnt, path + 1))
        
        return -1