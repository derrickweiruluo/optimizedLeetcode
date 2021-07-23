class Solution:
    # DFS
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        colors = {}
        
#         def dfs(idx, color):
#             if idx in colors:
#                 return colors[idx] == color
#             colors[idx] = color
#             for neigbor in graph[idx]:
#                 if not dfs(neigbor, 1 - color):
#                     return False
#             return True
        
#         for i in range(len(graph)):
#             if i not in colors:
#                 if not dfs(i, 99):
#                     return False

        
        for i in range(len(graph)):
            if i not in colors and graph[i]:
                colors[i] = 99
                queue = collections.deque([i])
                while queue:
                    curr = queue.popleft()
                    for neigbor in graph[curr]:
                        if neigbor not in colors:
                            colors[neigbor] = 1 - colors[curr]
                            queue.append(neigbor)
                        elif colors[neigbor] == colors[curr]:
                            return False
        
        return True
