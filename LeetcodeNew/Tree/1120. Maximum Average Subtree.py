'''
Given the root of a binary tree, return the maximum average value of a subtree of that tree. Answers within 10-5 of the actual answer will be accepted.

A subtree of a tree is any node of that tree plus all its descendants.

The average value of a tree is the sum of its values, divided by the number of nodes.

https://leetcode.com/problems/maximum-average-subtree/

'''

class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        
        def dfs(node):
            if not node:
                return 0, 0, 0 
            # treeSum, nodeCount, treeAvg
            # treeSum and nodeCount are used by parent tree, treeAvg is a local res
            left = dfs(node.left)
            right = dfs(node.right)
            
            treeSum = node.val + left[0] + right[0]
            nodeCount = 1 + left[1] + right[1]
            treeAvg = max(left[2], right[2], treeSum / nodeCount)
            
            return treeSum, nodeCount, treeAvg
        
        if not root: return 0
        return dfs(root)[2]
