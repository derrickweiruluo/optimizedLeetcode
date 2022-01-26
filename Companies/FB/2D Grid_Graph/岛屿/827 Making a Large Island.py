'''
You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

Return the size of the largest island in grid after applying this operation.

An island is a 4-directionally connected group of 1s.
'''

# https://leetcode.com/problems/making-a-large-island/discuss/127015/C%2B%2B-with-picture-O(n*m)

'''
https://leetcode.com/problems/making-a-large-island/discuss/127032/C%2B%2BJavaPython-Straight-Forward-O(N2)-with-Explanations

Explanation
Only 2 steps:

Only 2 steps:

1. Explore every island using DFS, count its area, give it an island index and save the result to a {index: area} map. Note the grid elements are updated with their corresponding island index. Since the grid has elements 0 or 1. The island index is initialized with 2

2. Loop every cell == 0, check its connected island index and calculate total islands area. The possible connected island index is stored in a set to remove duplicate index.

Complexity
Time O(N^2), N is the lwidth
Space O(N^2), additional space used in DFS and mapping of {islandId: area}
'''
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        
        def validCord(x, y): # yield a list of valid nearby indexes
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if 0 <= x + dx < m and 0 <= y + dy < n:
                    yield x + dx, y + dy
        
        def dfs(x, y, islandID):
            res = 1
            grid[x][y] = islandID
            for xi ,yi in validCord(x, y):
                if grid[xi][yi] == 1:
                    res += dfs(xi, yi, islandID)
            return res
        
        # step 1, mark all island from ID 2,3,4,etc
        islandID = 2        # input is 0, 1, change all 1 to 2,3,4,5,etc
        mapping = {0: 0}    # give all 0-index water with zero area
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    mapping[islandID] = dfs(i, j, islandID)
                    islandID += 1


        # step 2: loop all water, check if possible flip and update res

        # corner case，当当前已经有最大岛屿(没有case是flip one make bigger)
        res = max(mapping.values())

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    # use set below to prevent duplicate island (same ID)
                    nearbyIslandIDs = set(grid[x][y] for x, y in validCord(i, j))
                    res = max(res, 1 + sum(mapping[k] for k in nearbyIslandIDs))
        
        
        return res