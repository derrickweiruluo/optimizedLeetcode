'''
A Tree has such structure: the root is always the minimum of its two left and right node.

Indicate; root is the minimum

ASK: find the second miminum

'''

class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        
        '''
        More formally, the property root.val = min(root.left.val, root.right.val) always holds.
        '''
        self.res = math.inf
        
        def dfs(node):
            if not node:
                return
            if root.val < node.val < self.res:
                self.res = node.val
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return self.res if self.res != math.inf else -1