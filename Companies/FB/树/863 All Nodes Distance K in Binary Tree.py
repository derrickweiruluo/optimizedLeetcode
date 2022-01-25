'''
Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.
'''


# 看似Tree题，实际graph题

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        res = []
        graph = collections.defaultdict(list)
        visited = set()
        
        def dfs(node):  # 构建adjacency undirected graph of each node
            if not node: return
            if node.left:
                graph[node].append(node.left)
                graph[node.left].append(node)
                dfs(node.left)
            if node.right:
                graph[node].append(node.right)
                graph[node.right].append(node)
                dfs(node.right)
                
        def bfs(node, dist):
            if dist == 0:
                res.append(node.val)
            else:
                visited.add(node)
                for nextNode in graph[node]:
                    if nextNode not in visited:
                        bfs(nextNode, dist - 1)
        
        dfs(root)       # 遍历每个node，构建adjacency graph
        bfs(target, k)  # 这一步很重要，从target node出发往外BFS
        return res