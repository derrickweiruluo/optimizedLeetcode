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

Explore every island using DFS, count its area, give it an island index and save the result to a {index: area} map.
Loop every cell == 0, check its connected islands and calculate total islands area.

Complexity
Time O(N^2)
Space O(N^2)
'''
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        
        width = len(grid)
        
        def validNext(x, y):           # yield 相邻的坐标
            for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                if 0 <= x + i < width and 0 <= y + j < width:
                    yield x + i, y + j
        
        def dfs(x, y, islandID):       # 计算相邻大陆的面积
            res = 0
            grid[x][y] = islandID
            for i, j in validNext(x, y):
                if grid[i][j] == 1:
                    res += dfs(i, j, islandID)
            return res + 1
            
        islandID = 2
        mapping = {0 : 0}               # hashmap of 大陆ID: 面积
        for x in range(width):
            for y in range(width):
                if grid[x][y] == 1:
                    mapping[islandID] = dfs(x, y, islandID)
                    islandID += 1
        
        maxArea = max(mapping.values())   # corner case，当当前已经是最大的时候
        for x in range(width):            # 找非陆地，测试sum of (相邻面积 + 1)
            for y in range(width):
                if grid[x][y] == 0:
                    possibleNext = set(grid[i][j] for i, j in validNext(x, y))
                    maxArea = max(maxArea, sum(mapping[index] for index in possibleNext) + 1)
                    
        return maxArea