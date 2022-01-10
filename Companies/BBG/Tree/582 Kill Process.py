'''
You are given two integer arrays pid and ppid
pid[i] is the ID of the ith process
ppid[i] is the ID of the ith process's parent process.

Each process has only one parent process but may have multiple children processes. Only one process has ppid[i] = 0, which means this process has no parent process (the root of the tree).

When a process is killed, all of its children processes will also be killed.
'''


# 建立 parent node:[child node] 关系
# 通过parent -> child 一路向南kill下级的所有node

class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        
        mapping = collections.defaultdict(list)
        
        for parent, child in zip(ppid, pid):
            mapping[parent].append(child)
            
        res = []
        queue = collections.deque([kill])
        
        while queue:
            for _ in range(len(queue)):
                killed = queue.popleft()
                res.append(killed)
                
                if killed in mapping:  
                    # This is the way to extend a deque
                    # extend the BFS search to the end of the deque,
                    # while still popping from the left end, therefore BFS
                    queue.extend(mapping[killed])
        
        return res