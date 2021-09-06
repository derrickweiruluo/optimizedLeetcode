"""
In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

 

Example 1:

Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]

Example 2:

Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]
 

Constraints:

n == edges.length
3 <= n <= 1000
edges[i].length == 2
1 <= ai < bi <= edges.length
ai != bi
There are no repeated edges.
The given graph is connected.

"""
#### DSU with Path Compression and Ranking 模版
class DSU: 
    def __init__(self):
        self.parents = [i for i in range(1001)]
        self.ranks = [0] * 1001
        
    def find(self, val):
        if self.parents[val] != val:
            self.parents[val] = self.find(self.parents[val])
        return self.parents[val]
    
    def union(self, val1, val2):
      # union by rank, check whether union two vertics will lead to a cycle
        p1, p2 = self.find(val1), self.find(val2)
        if p1 == p2:  #找到第一个环
            return True
        elif self.ranks[p1] > self.ranks[p2]:
            self.parents[p2] = p1
        elif self.ranks[p1] < self.ranks[p2]:
            self.parents[p1] = p2
        else:
            self.ranks[p2] += 1
            self.parents[p1] = p2
        return False

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU()
        for edge in edges:
            if dsu.union(edge[0], edge[1]):
                return edge
            
