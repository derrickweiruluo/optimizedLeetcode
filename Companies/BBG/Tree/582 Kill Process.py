"""
Example 1:
Input:
pid =  [1, 3, 10, 5]
ppid = [3, 0, 5, 3]
kill = 5
Output: [5,10]
Explanation:
           3
         /   \
        1     5
             /
            10
Kill 5 will also kill 10.
Note:
The given kill id is guaranteed to be one of the given PIDs.
n >= 1.
"""
"""
Build a (int parent: list[int] children)hashMap and do a simple bfs.
"""



# Input: pid = [1,3,10,5], ppid = [3,0,5,3], kill = 5
# Output: [5,10]


# Clarifications: When a process is killed, all of its children processes will also be killed.
import collections
class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        
        # 建立 parent node:[child node] 关系
        mapping = collections.defaultdict(list)
        for parent, child in zip(ppid, pid):
            mapping[parent].append(child)
            
        res = []
        queue = collections.deque([kill])
        
        # 通过parent -> child 一路向南 BFS kill下级的所有node
        while queue:
            for _ in range(len(queue)):
                killed = queue.popleft()
                res.append(killed)
                
                if killed in mapping:  
                    # This is the way to extend a deque
                    # extend the BFS search to the end of the deque,
                    # while still popping from the left end, therefore BFS
                    queue.extend(mapping[killed])
                
                # 下面是一样的写法，简介点而已
                # queue.extend(mapping.get(deleted) or [])
        
        return res


# DFS
class Solution:
    def killProcess(self, pid, ppid, kill: int):
        graph = collections.defaultdict(list)
        for i, j in zip(ppid, pid):
            graph[i].append(j)

        res = []
        self.helper(graph, kill, res)
        return res

    def helper(self, graph, kill, res):
        res.append(kill)
        for i in graph[kill]:
            self.helper(graph, i, res)