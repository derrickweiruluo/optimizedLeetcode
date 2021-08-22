"""
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.



##########
O(n) 变形 num of island

"""


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        count, n = 0, len(isConnected)
        
        def dfs(grid, cur):
            for i in range(n):
                if grid[cur][i] == 1:
                    grid[cur][i] = grid[i][cur] = 0
                    dfs(grid, i)
        
        for i in range(n):
            if isConnected[i][i] == 1:
                count += 1
                dfs(isConnected, i)
                
        return count
