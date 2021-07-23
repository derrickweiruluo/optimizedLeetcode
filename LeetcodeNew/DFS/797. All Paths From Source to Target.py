# 基操

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
        
