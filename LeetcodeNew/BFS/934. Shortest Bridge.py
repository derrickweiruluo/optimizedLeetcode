"""
In a given 2D binary array grid, there are two islands.  (An island is a 4-directionally connected group of 1s not connected to any other 1s.)

Now, we may change 0s to 1s so as to connect the two islands together to form 1 island.
Return the smallest number of 0s that must be flipped.  (It is guaranteed that the answer is at least 1.)

 

Example 1:

Input: grid = [[0,1],[1,0]]
Output: 1
Example 2:

Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2
Example 3:

Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1
 

Constraints:
2 <= grid.length == grid[0].length <= 100
grid[i][j] == 0 or grid[i][j] == 1

#####思路
1. 先随机找到第一个点
2. 然后围绕着这个点，在grid内，把这个岛周边的海洋boundary，记录到一个hashset
2.1 dfs下一个相邻陆地，直到这个岛被search完，which意味着boundary也记录完
3. 把第一个岛屿的boundary来个BFS， return steps

注意： 以上的DFS， BFS步骤，每找到一块陆地都以第三方标记记录


"""
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        
        boundOne = set()  # to store boundary of the first found island
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rows, cols = len(grid), len(grid[0])
        
        def get_first():
            for i in range(rows):
                for j in range(cols):
                    if grid[i][j] == 1:
                        return (i, j)
        
        def dfs(i, j):  # to complete the boundary of the first island found above
            grid[i][j] = -1  # not dfs if mark as -1
            for dx, dy in dirs:
                xi, yi = i + dx, j + dy
                if 0 <= xi < rows and 0 <= yi < cols:
                    if grid[xi][yi] == 0:
                        boundOne.add((i, j))
                    elif grid[xi][yi] == 1:
                        dfs(xi, yi)
        
        steps = 0
        i, j = get_first(grid)
        dfs(grid, i, j)
        queue = collections.deque(list(boundOne))
        
        while queue:
            steps += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in dirs:
                    xi, yi = x + dx, y + dy
                    if 0 <= xi < m and 0 <= yi < n:
                        if grid[xi][yi] == 1:
                            return steps
                        elif grid[xi][yi] == 0:
                            queue.append((xi, yi))
                            grid[xi][yi] = -1
        
        return steps
