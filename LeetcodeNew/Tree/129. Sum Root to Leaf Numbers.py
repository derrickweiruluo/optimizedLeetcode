'''
You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.

'''

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        self.res = 0
        
        def dfs(node, path):
            if not node:
                return
            if not node.left and not node.right:
                self.res += path * 10 + node.val
            dfs(node.left, path * 10 + node.val)
            dfs(node.right, path * 10 + node.val)
        
        dfs(root, 0)
        return self.res
