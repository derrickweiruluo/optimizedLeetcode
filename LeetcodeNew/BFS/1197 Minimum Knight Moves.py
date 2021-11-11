'''
给一个 (x,y)坐标，骑士从(0,0)出发，问最少多少步可以到达


The basic idea is to make sure the total number of moves required always decrease if we move along the long edge.
I found the boundary 4 by drawing a graph, then solve the remaining number of steps by BFS.

https://leetcode.com/problems/minimum-knight-moves/discuss/540658/Python-greedy-%2B-bfs-solution-12ms-beats-100
'''

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        
        x, y = abs(x), abs(y)
        res = 0
        while x > 5 or y > 5: # greedy approach, can be any number, just to BFS start from closer
            res += 1
            if x > y:
                x -= 2
                y -= 1 if y >= 1 else -1    # when case x >> y,, to prevent go negative
            else:
                x -= 1 if x >= 1 else -1    # when case x >> y,, to prevent go negative
                y -= 2
        
        dirs = [(2,1), (2,-1), (-2,1), (-2,-1), (1,2), (1,-2), (-1,2), (-1,-2)]
        queue = collections.deque([(0, 0, 0)]) # queue of (cur_X, cur_Y, steps)
        while queue:
            i, j, steps = queue.popleft()
            if i == x and j == y:
                return res + steps
            for dx, dy in dirs:
                if (x - i) * dx > 0 or (y - j) * dy > 0:    # move towards (x, y) at least in one direction
                    queue.append((i + dx, j + dy, steps + 1))
        
        