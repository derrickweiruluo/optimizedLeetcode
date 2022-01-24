'''
https://leetcode.com/problems/maximum-path-quality-of-a-graph/

Input: values = [0,32,10,43], edges = [[0,1,10],[1,2,15],[0,3,10]], maxTime = 49
Output: 75
Explanation:
One possible path is 0 -> 1 -> 0 -> 3 -> 0. The total time taken is 10 + 10 + 10 + 10 = 40 <= 49.
The nodes visited are 0, 1, and 3, giving a maximal path quality of 0 + 32 + 43 = 75.

'''

class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        
        graph = collections.defaultdict(list)
        for u, v, time in edges:
            graph[u].append((v, time))
            graph[v].append((u, time))
        
        
        def dfs(node, visited, gain, rem):
            if node == 0:
                self.res = max(self.res, gain)
            for neighbor, c in graph[node]:
                if c <= rem:
                    # dfs(neighbor, visited | set([neighbor]), gain + (neighbor not in visited) * values[neighbor], rem - c)
                    dfs(neighbor, visited.union(set([neighbor])), gain + (neighbor not in visited) * values[neighbor], rem - c)
        
        self.res = 0
        dfs(0, set([0]), values[0], maxTime)
        return self.res
        