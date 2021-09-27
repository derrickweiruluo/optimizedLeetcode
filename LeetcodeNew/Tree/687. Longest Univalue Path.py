'''
Given the root of a binary tree, return the length of the longest path, where each node in the path has the same value. This path may or may not pass through the root.

The length of the path between two nodes is represented by the number of edges between them.
'''
# dfs，从底部开始update最优解并且同时判断左右子树是否valid

class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        
        if not root: return 0
        self.maxPath = 0
        
        def dfs(node):
            if not node: return 0            
            left = dfs(node.left)
            right = dfs(node.right)
            
            if node.left and node.left.val != node.val:
                left = 0
            if node.right and node.right.val != node.val:
                right = 0
            
            curPath = 1 + left + right
            self.maxPath = max(self.maxPath, curPath)
            return 1 + max(left, right)
        
        dfs(root)
        return self.maxPath - 1
        
