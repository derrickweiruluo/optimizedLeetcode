'''
You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.

Return true if the edges of the given graph make up a valid tree, and false otherwise.


There are no self-loops or repeated edges.ßß
'''

import collections
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # 无环graph的性质 # of nodes - 1 == # of edges
        if n - 1 != len(edges): return False
        
        graph = collections.defaultdict(set)
        for x, y in edges:
            graph[x].add(y)
            graph[y].add(x)
        
        stack = [0]
        visited = set()
        
        while stack:
            node = stack.pop()
            if node in visited:
                return False
            visited.add(node)
            for neighbor in list(graph[node]):
                stack.append(neighbor)
            #后两部是为了删除当前node的 进出directions
                graph[neighbor].remove(node)
            del graph[node]
        
        return not graph
            