"""
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
 

Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.


# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

##############
use dict[node] = Node(node.val) to create a copy
use visited to store visited nodes
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        def dfs(node, visited):
            if not node:
                return
            for neigh in node.neighbors:
                if neigh not in visited:
                    visited[neigh] = Node(neigh.val)
                    dfs(neigh, visited)
                visited[node].neighbors.append(visited[neigh])
        
        if not node:
            return
        visited = {node: Node(node.val)}
        dfs(node, visited)
        return visited[node]
