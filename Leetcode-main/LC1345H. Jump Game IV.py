class Solution:
    def minJumps(self, arr: List[int]) -> int:
        pos = {}
        for i, position in enumerate(arr):
            if position not in pos:
                pos[position] = []
            pos[position].append(i)
        
        bfs = [0]
        seen = set([0])
        n = len(arr)
        res = 0
        
        while bfs:
            bfs2 = []
            for i in bfs:
                if i == n - 1: return res
                for j in pos[arr[i]] + [i - 1, i + 1]:
                    if 0 <= j < n and j not in seen:
                        bfs2.append(j)
                        seen.add(j)
                pos[arr[i]] = []
            res += 1
            bfs = bfs2
        return res
                
        
