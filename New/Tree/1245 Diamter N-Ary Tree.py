'''
There is an undirected tree of n nodes labeled from 0 to n - 1. You are given a 2D array edges where edges.length == n - 1 and edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the tree.


Input: edges = [[0,1],[1,2],[2,3],[1,4],[4,5]]

     1
   / | \ 
   0 2  4
     |  |
     3  5

output = 4
'''

# Clarifications:
# n nodes labeled from 0 to n - 1. 
# Given a 2D array edges where edges.length == n - 1 and edges[i] = [ai, bi]

class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        
        n = len(edges) + 1
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        self.res = 0
        self.dfs(0, -1, graph) # root, parent, graph
        return self.res
    
    
    def dfs(self, node, parent, graph):
        maxDepthOne, maxDepthTwo = 0, 0
        for child in graph[node]:
            if child != parent:
                depth = self.dfs(child, node, graph)
                if depth > maxDepthOne:
                    maxDepthTwo = maxDepthOne
                    maxDepthOne = depth
                elif depth > maxDepthTwo:
                    maxDepthTwo = depth
        
        self.res = max(self.res, maxDepthOne + maxDepthTwo)
        return maxDepthOne + 1