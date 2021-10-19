'''
There are n computers numbered from 0 to n-1 connected by ethernet cables connections forming a network where connections[i] = [a, b] represents a connection between computers a and b. Any computer can reach any other computer directly or indirectly through the network.

Given an initial computer network connections. You can extract certain cables between two directly connected computers, and place them between any pair of disconnected computers to make them directly connected. Return the minimum number of times you need to do this in order to make all the computers connected. If it's not possible, return -1.


Input: n = 4, connections = [[0,1],[0,2],[1,2]]
Output: 1
Explanation: Remove cable between computer 1 and 2 and place between computers 1 and 3.

Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
Output: 2
'''


'''  # LEE
Explanation
We need at least n - 1 cables to connect all nodes (like a tree).
If connections.size() < n - 1, we can directly return -1.

One trick is that, if we have enough cables,
we don't need to worry about where we can get the cable from.

We only need to count the number of connected networks.
To connect two unconneccted networks, we need to set one cable.

The number of operations we need = the number of connected networks - 1


Complexity
Time O(connections)
Space O(n)


✨✨✨✨Constraints:
There are no repeated connections.
No two computers are connected by more than one cable.
'''

class Solution: # DFS
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        
        # The number of operations we need = the number of unconnected networks - 1
        if len(connections) < n - 1:  
            return -1
        
        graph = collections.defaultdict(set)
        visited = [0] * n
        for x, y in connections:
            graph[x].add(y)
            graph[y].add(x)
        
        def dfs(i):  # 沉没岛屿thru visited
            if visited[i]:
                return False
            visited[i] = 1
            for j in graph[i]:
                dfs(j)
            return True
        
        connectedNetworks = 0
        for i in range(n):
            if dfs(i):
                connectedNetworks += 1
        
        return connectedNetworks - 1

class Solution:  #UF
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        path = {}
        for i in range(n):
            path[i] = i
        def find(x):
            while x != path[x]:
                path[x] = path[path[x]]
                x = path[x]
            return x
        
        def union(x, y):
            pathX, pathY = find(x), find(y)
            if pathX == pathY:
                return False
            path[pathX] = pathY
            return True
        
        disconnected = n
        for x, y in connections:
            if union(x, y):
                disconnected -= 1
        
        # print(path)
        return disconnected - 1