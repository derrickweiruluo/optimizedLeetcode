"""
There is a ball in a maze with empty spaces (represented as 0) and walls (represented as 1). The ball can go through the empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the m x n maze, the ball's start position and the destination, where start = [startrow, startcol] and destination = [destinationrow, destinationcol], return true if the ball can stop at the destination, otherwise return false.

You may assume that the borders of the maze are all walls (see examples).

Constriants:
Both the ball and the destination exist in an empty space, and they will not be in the same position initially.
The maze contains at least 2 empty spaces.

"""

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        
        queue = collections.deque([(start[0], start[1])])
        visited = set((start[0], start[1]))
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m, n = len(maze), len(maze[0])
        
        while queue:
            x, y = queue.popleft()
            # Both the ball and the destination exist in an empty space, 
            # and they will not be in the same position initially
            if x == destination[0] and y == destination[1]:
                return True
            
            for dx, dy in dirs:
                xi, yi = x + dx, y + dy
                while 0 <= xi < rows and 0 <= yi < cols and maze[xi][yi] == 0:
                    xi, yi = xi + dx, yi + dy
                xi, yi = xi - dx, yi - dy
                # 这是走到尽头前的前一步，by BFS
                if (xi, yi) not in visited:
                    visited.add((xi, yi))
                    queue.append((xi, yi))
                    
        return False
