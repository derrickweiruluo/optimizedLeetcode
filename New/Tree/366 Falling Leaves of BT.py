

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = []  # [[], [], []]: level 0, 1, 2
        
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            depth = 1 + max(left, right)
            if depth > len(res):
                res.append([])
            res[depth - 1].append(node.val)
            return depth
        
        dfs(root)
        return res