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
