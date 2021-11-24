'''
Binary Tree 的最大深度，max depthß
'''

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        def dfs(node):
            if not node: return 0
            
            return 1 + max(dfs(node.left), dfs(node.right))
        
        return dfs(root)