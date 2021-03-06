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

class Solution(object): #other dfs + bfs
    def distanceK(self, root, target, K):
        def dfs(node, par = None):
            if node:
                node.par = par
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root)

        queue = collections.deque([(target, 0)])
        seen = {target}
        while queue:
            if queue[0][1] == K:
                return [node.val for node, d in queue]
            node, d = queue.popleft()
            for nei in (node.left, node.right, node.par):
                if nei and nei not in seen:
                    seen.add(nei)
                    queue.append((nei, d+1))

        return []

class Solution2:  # ONLY DFS
    def distanceK(self, root, target, K):
        adj, res, visited = collections.defaultdict(list), [], set()
        def dfs(node):
            if node.left:
                adj[node].append(node.left)
                adj[node.left].append(node)
                dfs(node.left)
            if node.right:
                adj[node].append(node.right)
                adj[node.right].append(node)
                dfs(node.right)
        dfs(root)
        def dfs2(node, d):
            if d < K:
                visited.add(node)
                for v in adj[node]:
                    if v not in visited:
                        dfs2(v, d + 1)
            else:
                res.append(node.val)
        dfs2(target, 0)
        return 