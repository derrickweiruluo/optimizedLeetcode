'''
Input: graph = [[1,2,3],[0],[0],[0]]
Output: 4
Explanation: One possible path is [1,0,2,0,3]
'''

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        memo, steps = set(), 0
        queue= [(i, 1 << i) for i in range(len(graph))]
        final = (1 << len(graph)) - 1
        
        '''        newstate = state | 1 << v
        Let our current state be state. We perform OR operation of 1 << v with our current state.
        This means that the node v will now be assigned visited if not already visited.

        Now why do we need to also store the node in the tuple too?
        Why can't we just use the state?
        This is because same states can be reached from different nodes too. So we must store the node too in the tuple.
        Hence we do

        memo.add((newstate, v))'''
        
        while True:
            nextLevel = []
            for node, state in queue:
                if state == final: return steps
                for v in graph[node]:
                    if (state | 1 << v, v) not in memo:
                        nextLevel.append((v, state | 1 << v))
                        memo.add((state | 1 << v, v))
            queue = nextLevel
            steps += 1