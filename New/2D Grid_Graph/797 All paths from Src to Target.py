'''
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.
'''

# I didn't do that in this problem, for the reason that it asks all paths. I don't expect memo to save much time. (I didn't test).
# Imagine the worst case that we have node-1 to node-N, and node-i linked to node-j if i < j.
# There are 2^(N-2) paths and (N+2)*2^(N-3) nodes in all paths. We can roughly say O(2^N).

import collections


# find path from o to n - 1 in a directed acyclic graph (DAG)
# Both O(n*2^n) ~ O(2^n)
class Solution: # LEEE
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        target = len(graph) - 1
        
        def dfs(cur_idx, path):
            if cur_idx == target:
                res.append(path)
            else:
                for next_idx in graph[cur_idx]:
                    dfs(next_idx, path + [next_idx])
        
        res = []
        dfs(0, [0])
        return res


# Iterative DFS
class Solution(object):
    def allPathsSourceTarget(self, graph):
        target = len(graph) - 1
        paths = collections.deque([[0]])
        res = []
        while paths:
            path = paths.popleft()
            for i in graph[path[-1]]:
                if i == target:
                    res.append(path + [i])
                else:
                    paths.append(path + [i])
        return res


# BFS
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        queue = collections.deque([(0, [0])])
        target = len(graph) - 1
        while queue:
            cur,route = queue.popleft()
            if cur == target:
                res.append(route)
            else:
                for node in graph[cur]:
                    queue.append((node, route + [node]))
        return res