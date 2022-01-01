'''
Given the root of a binary tree, return the maximum path sum of any non-empty path.
'''

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.res = -math.inf
        
        def dfs(node):
            if not node:
                return 0
            left = max(0, dfs(node.left))       # 往上递归 只递归 > 0 的branch
            right = max(0, dfs(node.right))     # 往上递归 只递归 > 0 的branch
            # 来保障由下往上，一直返回最优解


            self.res = max(self.res, node.val + left + right)
            # self.res = max(self.res, node.val + max(0, left) + max(0, right))
            return node.val + max(left, right)
        
        dfs(root)
        return self.res