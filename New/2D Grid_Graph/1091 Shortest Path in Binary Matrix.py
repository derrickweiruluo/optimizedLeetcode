'''
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

'''


# Clarificaitons: 
# All the visited cells of the path are 0.
# All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).


class Solution:  # BEST, 双向 BFS
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        
        def validCord(x, y): # yield a list of valid nearby indexes
            for dx, dy in [(1, 0), (0, 1), (1, 1)]:
                if 0 <= x + dx < m and 0 <= y + dy < n:
                    yield x + dx, y + dy
        
        m, n = len(grid), len(grid[0])
        # dirs = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1),  (-1, -1), (-1, 1)]
        # dirs = [(1, 0), (0, 1), (1, 1)]  # 尽管可以走8个方向，但其实只有3个方向可以走
        front, back = {(0, 0)}, {(m - 1, n - 1)}
        dist = 0
        
        while front:
            dist += 1
            next_front = set()
            for x, y in front:
                for xi, yi in validCord(x, y):
                    if (xi, yi) in back:
                        return dist
                    next_front.add((xi, yi))
            front = next_front
            if len(back) < len(front):
                front, back = back, front
        
        return 0



class Solution:   # 正常 BFS
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        # corner case, 起点终点都堵住了
        if grid[0][0] == 1 or grid[-1][-1] == 1: return -1
        

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1),  (-1, -1), (-1, 1)]
        m, n = len(grid), len(grid[0])
        
        visited = set()
        visited.add((0, 0))
        ß
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