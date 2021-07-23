class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        nodeDict = {i: set() for i in range(n)}
        
        for i, j in edges:
            nodeDict[i].add(j)
            nodeDict[j].add(i)
        
        firstKey = list(nodeDict.keys())[0]
        stack = [firstKey]
        visited = set()
        
        while stack:
            node = stack.pop()
            if node in visited:
                return False
            visited.add(node)
            for neighbor in nodeDict[node]:
                stack.append(neighbor)
                nodeDict[neighbor].remove(node)
            
            nodeDict.pop(node)
        
        return not nodeDict
