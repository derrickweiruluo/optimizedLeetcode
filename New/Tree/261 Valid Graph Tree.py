'''
You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.

Return true if the edges of the given graph make up a valid tree, and false otherwise.
'''

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if n - 1 != len(edges): return False
        graph = collections.defaultdict(set)
        for u, v in edges:
            graph[v].add(u)
            graph[u].add(v)
        
        stack = [0]
        visited = set()
        
        while stack:
            node = stack.pop()
            if node in visited:
                return False
            visited.add(node)
            for neighbor in graph[node]:
                stack.append(neighbor)
                graph[neighbor].remove(node)
            del graph[node]
        
        return not graph
        

        
#         key = 0: [1,2,3]
#         key = 1: [0, 4]
#         key = 2: [0]
#         key = 3: [0]
#         key = 4: [1]
            
#         stack[0] 
#         pop(0) --> for loop [1,2,3], delete : 1-0, 2-0, 3-0, lastly delete graph[0]
#         stack[1,2,3]
#         pop(1) --> for loop [4], delete: 4-1, lastly delete graph[1]
#         stack[2,3,4]
#         pop(2) --> for loop  空了, delete graph[2]
#         stack[3,4]
#         pop(3) --> for loop  空了，delete graph[3]
#         stack[4]
#         pop(4) --> for loop 空了， delete gragh[4]
        
#         最后check graph is null