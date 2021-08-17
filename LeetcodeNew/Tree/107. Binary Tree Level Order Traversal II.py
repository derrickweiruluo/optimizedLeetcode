"""
Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. (i.e., from left to right, level by level from leaf to root).

层级遍历，最后[::-1]
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root: return []
        
        res = []
        cur_level = [root]
        
        while cur_level:
            next_level = []
            cur_val = []
            for node in cur_level:
                cur_val.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            
            res.append(cur_val)
            cur_level = next_level
        
        return res[::-1]
