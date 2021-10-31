'''
Example 1:

Input: adjacentPairs = [[2,1],[3,4],[3,2]]
Output: [1,2,3,4]
Explanation: This array has all its adjacent pairs in adjacentPairs.
Notice that adjacentPairs[i] may not be in left-to-right order.
Example 2:

Input: adjacentPairs = [[4,-2],[1,4],[-3,1]]
Output: [-2,4,1,-3]
Explanation: There can be negative numbers.
Another solution is [-3,1,4,-2], which would also be accepted.
Example 3:

Input: adjacentPairs = [[100000,-100000]]
Output: [100000,-100000]

'''  #Leetcode 1743
import collections
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        
        graph = collections.defaultdict(list)
        for x, y in adjacentPairs:
            graph[x].append(y)
            graph[y].append(x)
        
        def dfs(num):
            res.append(num)
            visited[num] = True
            for adj in graph[num]:
                if not visited[adj]:
                    dfs(adj)
        
        outer = [x for x in graph if len(graph[x]) == 1]
        visited = {x: False for x in graph}
        res = []
        dfs(outer[0])
        return res