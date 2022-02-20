'''
LCA of all deepest Nodes

Same as 1123
'''

# Clarifications:
# The values of the nodes in the tree are unique.
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        
        self.deepest = 0
        self.LCA = None
        
        def dfs(node, depth):
            self.deepest = max(self.deepest, depth)
            if not node:
                return depth
            left = dfs(node.left, depth + 1)
            right = dfs(node.right, depth + 1)
            
            if left == right == self.deepest: # 每次想上返回时，LCA可能被update成更上层的node，根据上层node 左右子树的长度
                self.LCA = node
            return max(left, right)
        
        dfs(root, 0)
        return self.LCA