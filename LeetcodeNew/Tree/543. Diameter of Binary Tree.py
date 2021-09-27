'''
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.
'''


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        if not root: return 0
        
        self.depth = 1
        
        def dfs(node):
            if not node: return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.depth = max(self.depth, 1+ left + right)
            return 1 + max(left, right)
        
        dfs(root)
        
        # return depth - 1 is because #edges = depth - 1 
        return self.depth - 1
