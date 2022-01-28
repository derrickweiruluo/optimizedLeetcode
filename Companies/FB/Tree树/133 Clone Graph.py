'''
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.
'''


#### Clarification to make
# Node.val is unique for each node.
# There are no repeated edges and no self-loops in the graph.
# The Graph is connected and all nodes can be visited starting from the given node
# For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

'''
https://leetcode.com/problems/clone-graph/discuss/42314/Python-solutions-(BFS-DFS-iteratively-DFS-recursively).

# O(V + E)
# O(N): O(N and H), but N is dominating the space in recursive stack
'''
import collections

#### Clarification to make
# Node.val is unique for each node.
# There are no repeated edges and no self-loops in the graph.
# The Graph is connected and all nodes can be visited starting from the given node

class Solution:  # BFS Iterative
    # O(V + E), O(N) space
    def cloneGraph(self, node: 'Node') -> 'Node':
        queue = collections.deque([node])
        mapping = {node: Node(node.val)}
        
        while queue:
            cur = queue.popleft()
            for neighbor in cur.neighbors:
                if neighbor not in mapping:
                    queue.append(neighbor)
                    mapping[neighbor] = Node(neighbor.val)
                mapping[cur].neighbors.append(mapping[neighbor])
        
        return mapping[node]

#######
# # O(V + E), O(N) space
class Solution:  # DFS recursive
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        def dfs(node, graph):
            if not node:
                return
            for neighbor in node.neighbors:
                if neighbor not in graph:
                    graph[neighbor] = Node(neighbor.val)
                    dfs(neighbor, graph)
                graph[node].neighbors.append(graph[neighbor])
                
        
        if not node: 
            return
        graph = {node: Node(node.val)}
        dfs(node, graph)
        return graph[node]

###

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

        ####

class Solution:  # BFS Iterative
    # O(V + E), O(N) space

    def cloneGraph(self, node: 'Node') -> 'Node':
        queue = collections.deque([node])
        mapping = {node: Node(node.val)}
        
        while queue:
            cur = queue.popleft()
            for neighbor in cur.neighbors:
                if neighbor not in mapping:
                    queue.append(neighbor)
                    mapping[neighbor] = Node(neighbor.val)
                mapping[cur].neighbors.append(mapping[neighbor])
        
        return mapping[node]


