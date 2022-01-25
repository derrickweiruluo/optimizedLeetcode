'''
You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

Return the number of connected components in the graph.


Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2

0 -- 1        3
     |        |
     |        |
     2        4

Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
Output: 1

0 -- 1        3
     |     /  |
     |  /     |
     2        4
'''

# Time: O(n+m), where m is the number of connections, n is the number of nodes.
# Space: O(n)
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:        
        # res = n
        res = 0
        rank = [1] * n  # optimization for path compression
        parent = [-1] * n         # nums[i] is the root of i
        for u, v in edges:      # union each u-v edge
            self.union(u, v, parent, rank)
        
        for p in parent:
            if p == -1: res += 1
        return res
    
    def find(self, parent, i):
        if parent[i] == -1:
            return i
        return self.find(parent, parent[i])
    
    # def union(self, parent, u, v):
    #     x, y = self.find(parent, u), self.find(parent, v)
    #     if x == y:
    #         return False
    #     parent[x] = y
    #     return True


    def union(self, x, y, parent, rank):  # With ranking
        rx, ry = self.find(parent, x), self.find(parent, y)
        if rx == ry:
            return
        if rank[rx] > rank[ry]:
            parent[ry] = rx
        elif rank[rx] < rank[ry]:
            parent[rx] = ry
        else:
            parent[rx] = ry
            rank[ry] += 1


# DFS
# Time: O(n+m), where m is the number of connections, n is the number of nodes.
# Space: O(n+m)
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = [0] * n
        res = 0
        
        def dfs(graph, i):
            if visited[i]:
                return
            visited[i] = 1
            for j in graph[i]:
                dfs(graph, j)
        
        for i in range(n):
            if not visited[i]:
                dfs(graph, i)
                res += 1
        
        return res