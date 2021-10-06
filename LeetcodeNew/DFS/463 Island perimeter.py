'''
给有且仅有一个island, 求这个岛屿的总边长
'''

# 思路：
# 0. 总边长最初是 陆地数 * 4
# 1. skip 掉第一行和第一列 (看笔记本)
# 2A. 如果左边有陆地：边长 -= 2
# 2B. 如果上边有陆地：边长 -= 2
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res += 4
                    if i > 0 and grid[i - 1][j] == 1:
                        res -= 2
                    if j > 0 and grid[i][j - 1] == 1:
                        res -= 2
        
        return res