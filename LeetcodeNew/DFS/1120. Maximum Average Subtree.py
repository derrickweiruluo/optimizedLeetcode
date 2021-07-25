# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        
        def dfs(node):
            if not node:
                return 0, 0, 0    # subtree sum, subtree node count, average
            left = dfs(node.left)
            right = dfs(node.right)
            
            curr_sum = left[0] + right[0] + node.val
            num_nodes = left[1] + right[1] + 1
            max_average = max(left[2], right[2], curr_sum / num_nodes)
            
            return curr_sum, num_nodes, max_average
        
        return dfs(root)[2]
