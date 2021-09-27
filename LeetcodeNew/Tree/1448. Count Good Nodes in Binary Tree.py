'''
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

Constraints:

The number of nodes in the binary tree is in the range [1, 10^5].
Each node's value is between [-10^4, 10^4].

####数的信息传递
每次层传递node.next, max(node.val, prevMax)
'''

class Solution #1:
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root, root.val)
    
    def dfs(self, node, prevMax):
        res = 0
        if not node:
            return 0
        if node.val >= prevMax:
            res += 1
        res += self.dfs(node.left, max(node.val, prevMax))
        res += self.dfs(node.right, max(node.val, prevMax))
        return res
        
# def dfs(self, node, prevMax):  
#         if not node: return
#         if node.val >= prevMax:
#             self.goodNodeCount += 1
#         self.dfs(node.left, max(node.val, pervMax))
#         self.dfs(node.right, max(node.val, pervMax))        
        
class Solution #2:
    def goodNodes(self, root: TreeNode) -> int: 
        self.res = 0
        self.dfs(root, root.val)
        return self.res
    
    def dfs(self, node, prevMax):
        if node.val >= prevMax:
            self.res += 1
        if node.left:
            self.dfs(node.left, max(prevMax, node.val))
        if node.right:
            self.dfs(node.right, max(prevMax, node.val))
