'''
You are given an m x n grid grid of values 0, 1, or 2, where:

each 0 marks an empty land that you can pass by freely,
each 1 marks a building that you cannot pass through, and
each 2 marks an obstacle that you cannot pass through.
You want to build a house on an empty land that reaches all buildings in the shortest total travel distance. You can only move up, down, left, and right.

Return the shortest travel distance for such a house. If it is not possible to build such a house according to the above rules, return -1.

The total travel distance is the sum of the distances between the houses of the friends and the meeting point.

Constraints::
grid[i][j] is either 0, 1, or 2.
There will be at least one building in the grid.
'''



class Solution1:  
    # https://leetcode.com/problems/shortest-distance-from-all-buildings/discuss/76877/Python-solution-72ms-beats-100-BFS-with-pruning
    # BEST, Eealry return when notice a building can not each all other buildings
    # Both solutions are: O(B * NM)
    # Space O(NM), distSum, visited

    '''
    Does anyone want to ask Why don't we start from '0'? This is also what I am thinking. At the first glance, the time complexity of starting from buildings O(B*M*N) (B: # of buildings) and starting from empty places O(E*M*N) (E: # of empty places) might be the same. If in an interview, I think we can ask for clarification. If the empty places are far more than buildings, ex. we have 1 million empty places and only 1 building, starting from building is better. So it depends on how many empty places and buildings that we have. We are not going to say this way or that way is better, but it's a kind of trade-off.
    '''

    def shortestDistance(self, grid: List[List[int]]) -> int:
        
        if not grid or not grid[0]: return -1
        m, n = len(grid), len(grid[0])
        buildingCnt = sum(val for r in grid for val in r if val == 1)
        distSum = collections.defaultdict(list) # 记录每一块空地到bldg 的list of [dist]
        res = math.inf
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:  # start BFS from building
                    if not self.bfs(grid, i, j, distSum, buildingCnt):
                        return -1
        
        for (i, j), lst in distSum.items():
            # 如果某一块空地 可达到所有building， update res
            if len(lst) == buildingCnt:
                res = min(res, sum(lst))

        return res if res != math.inf else -1
    
    
    def bfs(self, grid, i, j, distSum, cnt):
        # BFS from a building, access all empty space
        # on each visited empty space, store dict {position: dist_to_bldg}
        queue = collections.deque([(i, j, 0)])
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        visited[i][j] = True
        res = 1
        while queue:
            x, y, dist = queue.popleft()
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                xi, yi = x + dx, y + dy
                if 0 <= xi < len(grid) and 0 <= yi < len(grid[0]) and not visited[xi][yi]:
                    visited[xi][yi] = True
                    if grid[xi][yi] == 0:
                        distSum[(xi, yi)].append(dist + 1)
                        queue.append((xi, yi, dist + 1))
                    elif grid[xi][yi] == 1:
                        res += 1
        return res == cnt


##################
import collections, math
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        distSum = [[0] * n for _ in range(m)]
        hit = [[0] * n for _ in range(m)]
        
        buildingCnt = 0
        
        for i in range(m):
            for j in range(n):
                # if there is a building update reach, distance for all zeros using BFS
                if grid[i][j] == 1:
                    buildingCnt += 1
                    queue = collections.deque([(i, j, 0)])
                    
                    visited = [[False] * n for _ in range(m)]
                    
                    while queue:
                        x, y, dist = queue.popleft()
                        for dx, dy in dirs:
                            xi, yi = x + dx, y + dy
                            if 0 <= xi < m and 0 <= yi < n and grid[xi][yi] == 0 and not visited[xi][yi]:
                                distSum[xi][yi] += dist + 1
                                hit[xi][yi] += 1
                                visited[xi][yi] = True
                                queue.append((xi, yi, dist + 1))

        shortest = math.inf
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and hit[i][j] == buildingCnt:
                    shortest = min(shortest, distSum[i][j])
        
        return shortest if shortest != math.inf else -1