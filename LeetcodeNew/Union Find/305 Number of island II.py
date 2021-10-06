'''
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

'''

class Solution:
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