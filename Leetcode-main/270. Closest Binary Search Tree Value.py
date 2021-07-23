# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        
        res = root.val
        
        while root:
            if abs(root.val - target) < abs(res - target):
                res = root.val
            root = root.left if root.val > target else root.right
        
        return res
