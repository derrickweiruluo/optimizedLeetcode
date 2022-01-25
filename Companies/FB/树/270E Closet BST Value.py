'''
Given the root of a binary search tree and a target value, return the value in the BST that is closest to the target
'''


class Solution(object):
    def closestValue(self, root, target):
        cur = root
        res = cur.val
        while cur:
            if abs(cur.val - target) < abs(res - target):
                res = cur.val
            if cur.val == target:
                return cur.val
            elif cur.val < target:
                cur = cur.right
            else:
                cur = cur.left
        return res


class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        
        res = root.val
        
        while root:
            if abs(root.val - target) < abs(res - target):
                res = root.val
            root = root.left if root.val > target else root.right
        
        return res