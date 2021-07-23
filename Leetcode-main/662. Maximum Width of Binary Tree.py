# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        
        if not root: return 0
        
        queue = [(root, 0)]
        res = 0
        while queue:
            res = max(res, queue[-1][1] - queue[0][1] + 1)
            next_level = []
            for node, pos in queue:
                if node.left:
                    next_level.append((node.left, pos * 2))
                if node.right:
                    next_level.append((node.right, pos * 2 + 1))
                    
            queue = next_level
            
        return res
