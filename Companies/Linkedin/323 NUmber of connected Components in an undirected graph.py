"""
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes),
write a function to find the number of connected components in an undirected graph.
Example 1:
Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]
     0          3
     |          |
     1 --- 2    4
Output: 2
Example 2:
Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
     0           4
     |           |
     1 --- 2 --- 3
Output:  1
Note:
You can assume that no duplicate edges will appear in edges.
Since all edges are undirected, [0, 1] is the same as [1, 0]
and thus will not appear together in edges.
"""


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = collections.defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
            
        visited = [0]* n
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


class Solution:  #UF
    def countComponents(self, n: int, edges) -> int:
        result = n
        nums = [-1] * n
        for u, v in edges:
            if self.union(nums, u, v):
                result -= 1
        return result

    def find(self, nums, i):
        if nums[i] == -1:
            return i
        return self.find(nums, nums[i])

    def union(self, nums, i, j):
        x, y = self.find(nums, i), self.find(nums, j)
        if x == y:
            return False
        nums[x] = y
        return True