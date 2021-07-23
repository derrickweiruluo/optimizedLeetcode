# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        
        max_path = -math.inf
        
        def get_max_gain(node):
            nonlocal max_path # for node, we are updating the global 解
            if not node:
                return 0
            
            left_max_gain = max(0, get_max_gain(node.left))
            right_max_gain = max(0, get_max_gain(node.right))
            
            curr_max = node.val + left_max_gain + right_max_gain # curr node's max
            max_path = max(max_path, curr_max)  # update the gloabl max_path, 
            
            return node.val + max(left_max_gain, right_max_gain) # for each node, that is the 解
        
        get_max_gain(root)
        
        return max_path
