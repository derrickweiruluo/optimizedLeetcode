'''
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

Constraints:

The number of nodes in the binary tree is in the range [1, 10^5].
Each node's value is between [-10^4, 10^4].

####数的信息传递
每次层传递node.next, max(node.val, prevMax)
'''

class Solution: #1
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root, root.val)
    
    def dfs(self, node, prevMax): # return numbers of good node, root + left + right
        goodCount = 0
        if not node:
            return 0
        if node.val >= prevMax:
            goodCount += 1
        goodCount += self.dfs(node.left, max(node.val, prevMax))
        goodCount += self.dfs(node.right, max(node.val, prevMax))
        
        return goodCount
        
# def dfs(self, node, prevMax):  
#         if not node: return
#         if node.val >= prevMax:
#             self.goodNodeCount += 1
#         self.dfs(node.left, max(node.val, pervMax))
#         self.dfs(node.right, max(node.val, pervMax))        
        
class Solution2: #2
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

class Solution3: #3
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(root, preMax):
            if not root:
                return
            if root.val >= preMax:
                self.res += 1
            dfs(root.left, max(root.val, preMax))
            dfs(root.right, max(root.val, preMax))
        
        dfs(root, -math.inf)
        return self.res