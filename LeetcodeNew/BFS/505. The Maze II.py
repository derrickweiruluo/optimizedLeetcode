"""
There is a ball in a maze with empty spaces (represented as 0) and walls (represented as 1). The ball can go through the empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the m x n maze, the ball's start position and the destination, where start = [startrow, startcol] and destination = [destinationrow, destinationcol], return the shortest distance for the ball to stop at the destination. If the ball cannot stop at destination, return -1.

The distance is the number of empty spaces traveled by the ball from the start position (excluded) to the destination (included).

You may assume that the borders of the maze are all walls (see examples).

Constraints:
Both the ball and the destination exist in an empty space, and they will not be in the same position initially.
The maze contains at least 2 empty spaces.

思路：
1. 这道题是指球在迷宫里滚，假如没有障碍物是停不下来的
2. 用heapq.heappop(queue) & heappush(queue, (queue item)) 来保持BFS所用的queue的头部永远是最短路径(min heap)
3. queue of (dist, x, y)
"""
class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        
        m, n = len(maze), len(maze[0])
        queue = [(0, start[0], start[1])]
        visited = {(start[0], start[1]): 0}
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        # only use queue is because to always get the next distance thru HeapQueue
        
        while queue:
            dist, x, y = heapq.heappop(queue)
            if [x, y] == destination: 
                return dist
            for dx, dy in dirs:
                xi, yi, addedDist = x + dx, y + dy, 1
                while 0 <= xi < m and 0 <= yi < n and maze[xi][yi] != 1:
                    xi += dx
                    yi += dy
                    addedDist += 1
                # hittign a wall means the last added (dx, dy and addedDist) needs to subtract back
                xi -= dx
                yi -= dy
                addedDist -= 1
                if (xi, yi) not in visited or dist + addedDist < visited[(xi, yi)]:
                    visited[(xi, yi)] = dist + addedDist
                    heapq.heappush(queue, (dist + addedDist, xi, yi))
        
        return -1
