'''
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.
'''
import collections

# Both O(n*2^n)
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        last_idx = len(graph) - 1
        
        def dfs(cur_idx, path):
            if cur_idx == last_idx:
                res.append(path)
            else:
                for next_idx in graph[cur_idx]:
                    dfs(next_idx, path + [next_idx])
        
        res = []
        dfs(0, [0])
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