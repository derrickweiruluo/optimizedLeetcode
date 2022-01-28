'''
Find a leaf node, that is cloest to the target node

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findClosestLeaf(self, root: Optional[TreeNode], k: int) -> int:
        
        # where every node has a unique value and a target integer k
        # return the value of the nearest leaf node to the target k in the tree.
        
        # Step 1: 父子关系表，比以往的有点不同，要考虑 null 和 root's parent
        # root's parent is Null
        # 不完整的 node 的 孩子也是两个 (left/right, null), for length checking
        graph = collections.defaultdict(list)
        def dfs(node, par = None):
            if node:
                graph[node].append(par)
                graph[par].append(node)
                dfs(node.left, node)
                dfs(node.right, node)
        
        dfs(root)

        # Step 2: Queue start with node K
        queue = collections.deque([])
        for node in graph:
            if node and node.val == k:
                queue.append(node)
        
        visited = set(queue)

        # BFS, if len of list of child nodes == 1: leave
        while queue:
            node = queue.popleft()
            if node:
                if len(graph[node]) == 1:
                    return node.val
                for nei in graph[node]:
                    if nei not in visited:
                        visited.add(nei)
                        queue.append(nei)