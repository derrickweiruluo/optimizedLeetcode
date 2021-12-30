'''
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.
'''

class Solution: # Time O(N), Space O(K)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        # The diameter of a BT is the length of the longest path between any two nodes in a tree. 
        # This path may or may not pass through the root.
        
        self.res = 0
        
        if not root:
            return 0
        
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.res = max(self.res, 1 + left + right)
            return 1 + max(left, right)
        
        dfs(root)
        return self.res - 1