"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.


"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0            # 0 depth
        if not root.left and not root.right:
            return 1            # 1 depth, only has the root
        if root.left and not root.right:
            return 1 + self.minDepth(root.left)     # 1  + depth of root.left
        if root.right and not root.left:
            return 1 + self.minDepth(root.right)    # 1  + depth of root.right
        
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))   # 1  + depth of min subtree depth