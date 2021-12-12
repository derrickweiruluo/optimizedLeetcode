

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
Note: This is a BST
Avoid meaningless search

only visit left-subtree if node.val > low
only visit right-subtree if node.val < high
The valid range is [low, high]:: inclusive!!!
'''

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        self.res = 0
        
        def dfs(node, lo, hi):
            if not node: return
            if lo <= node.val <= hi:
                self.res += node.val
            if node.val > lo:
                dfs(node.left, lo, hi)
            if node.val < hi:
                dfs(node.right, lo, hi)
        
        dfs(root, low, high)
        return self.res