"""
You are given an empty 2D binary grid grid of size m x n. The grid represents a map where 0's represent water and 1's represent land. Initially, all the cells of grid are water cells (i.e., all the cells are 0's).

We may perform an add land operation which turns the water at position into a land. You are given an array positions where positions[i] = [ri, ci] is the position (ri, ci) at which we should operate the ith operation.

Return an array of integers answer where answer[i] is the number of islands after turning the cell (ri, ci) into a land.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

#########

Union Find
Time complexity : O(m * n + L)O(m×n+L) where LL is the number of operations, mm is the number of rows and nn is the number of columns. it takes O(m \times n)O(m×n) to initialize UnionFind, and O(L)O(L) to process positions. Note that Union operation takes essentially constant time[1] when UnionFind is implemented with both path compression and union by rank.

Space complexity : O(m * n)O(m×n) as required by UnionFind data structure.



"""


class Solution:
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
            path[path_x] = path_y.  # connect if not in the same path
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
        
