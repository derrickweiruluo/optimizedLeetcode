'''
Given the root of a binary search tree and a target value, return the value in the BST that is closest to the target
'''

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        
        res = root.val
        
        while root:
            if abs(root.val - target) < abs(res - target):
                res = root.val
            root = root.left if root.val > target else root.right
        
        return res