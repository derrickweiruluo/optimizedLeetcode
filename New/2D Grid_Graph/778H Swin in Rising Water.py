'''
grid[i][j] 代表 这个格子的boundary高度

(0, 0)出发，请问多久可以到达 (-1, -1)

Return the least time until you can reach the bottom right square (n - 1, n - 1) if you start at the top left square (0, 0).
'''


# time complexity: O(n^2*logn)

# pq contains at most n^2 elements, pop time complexity each time is is O(logn^2) = O(2*logn)
# At most we will pop n^2 times
# O(n^2*2*logn) = O(n^2*logn)
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        heap = [(grid[0][0], 0, 0)]
        visited = set([(0, 0)])
        res = 0
        
        while True:
            time, x, y = heapq.heappop(heap)
            res = max(res, time)
            if x == y == n - 1:
                return res
            for xi, yi in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= xi < n and 0 <= yi < n and (xi, yi) not in visited:
                    visited.add((xi, yi))
                    heapq.heappush(heap, (grid[xi][yi], xi, yi))