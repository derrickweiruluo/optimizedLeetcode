"""
2D Grid

Example1 1:
Input: m = 3, n = 3, positions = [[0,0],[0,1],[1,2],[2,1]]
Output: [1,1,2,3]
Explanation:
Initially, the 2d grid is filled with water.
- Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land. We have 1 island.
- Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land. We still have 1 island.
- Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land. We have 2 islands.
- Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land. We have 3 islands.

Example 2:
Input: m = 1, n = 1, positions = [[0,0]]
Output: [1]


#########
Union Find
Time complexity : O(m * n + L)O(m×n+L) where LL is the number of operations, mm is the number of rows and nn is the number of columns. it takes O(m \times n)O(m×n) to initialize UnionFind, and O(L)O(L) to process positions. Note that Union operation takes essentially constant time[1] when UnionFind is implemented with both path compression and union by rank.
Space complexity : O(m * n)O(m×n) as required by UnionFind data structure.
"""
class Solution1:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        path = {}
        seen = set()
        res, count = [], 0
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for x, y in positions:
            if (x, y) not in seen:
                seen.add((x, y))
                count += 1
                for dx, dy in dirs:
                    xi, yi = x + dx, y + dy
                    # 相邻且不同path, UF operation, update path
                    if (xi, yi) in seen and self.union((xi, yi), (x, y), path):
                        count -= 1
            res.append(count)
        return res
    
    def union(self, x, y, path):
        pathX, pathY = self.find(x, path), self.find(y, path)
        if pathX == pathY:
            return False
        path[pathX] = pathY
        return True
    
    def find(self, x, path):
        while x in path:
            if path[x] in path:
                path[x] = path[path[x]]
            x = path[x]
        return x

''' Almost the same solution'''

class Solution2:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        
        def find(x): 
            while x in path:
                if path[x] in path:   # path compression to root node
                    path[x] = path[path[x]]
                x = path[x]
            return x
    
        def union(x, y):
            path_x, path_y = find(x), find(y)
            if path_x == path_y:
                return False
            path[path_x] = path_y  # connect if not in the same path
            # path[path_y] = path_x
            return True
        
        seen, path, res, count = set(), dict(), [], 0
        
        for x, y in positions:
            if (x, y) not in seen:
                seen.add((x, y))
                count += 1
                for xi, yi in [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)]:
                    # if the neighbor not visited and these two neighbor not from the same path, union and count -=1
                    if (xi, yi) in seen and union((xi, yi), (x, y)):
                        count -= 1
        
            res.append(count)
            
        return res
        
