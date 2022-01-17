'''
# 算 唯一岛屿的周长

grid = [
    [0,1,0,0],
    [1,1,1,0],
    [0,1,0,0],
    [1,1,0,0]]


res = 4 + 4 + (4 - 4) + 2 + 2 + 4 + (4 - 4)
'''



# Clarifications:
# 1.    有且仅有一次岛屿
# 2.    岛屿garantee里面没有任何的水，全由陆地组成  

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res += 4
                    # check i > 0 and j > 0 因为我们 从右下两条边查重
                    # 以左上角有参照物，之比较 row - 1 and col - 1 的情况来做增减
                    if i > 0 and grid[i - 1][j] == 1:
                        res -= 2
                    if j > 0 and grid[i][j - 1] == 1:
                        res -= 2
        
        return res