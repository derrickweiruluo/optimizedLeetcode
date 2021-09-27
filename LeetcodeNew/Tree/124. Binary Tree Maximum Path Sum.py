'''
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any path.


#####
https://leetcode.com/problems/binary-tree-maximum-path-sum/
每个树是一个部分解，每个node return 当前node + max(左右子树)
'''
class Solution #1:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.maxPath = -math.inf
        self.dfs(root)
        return self.maxPath
    
    def dfs(self, node):
        if not node: 
            return 0
        left = max(0, self.dfs(node.left))
        right = max(0, self.dfs(node.right))
        
        curMax = node.val + left + right
        self.maxPath = max(self.maxPath, curMax)
        return node.val + max(left, right)


class Solution #2:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.maxPath = -math.inf
        
        def dfs(node):
            if not node:
                return 0
            leftSum = max(0, dfs(node.left))
            rightSum = max(0, dfs(node.right))
            
            subTreeSum = node.val + leftSum + rightSum
            self.maxPath = max(self.maxPath, subTreeSum)
            
            return node.val + max(leftSum, rightSum)
            
        
        dfs(root)
        return self.maxPath
