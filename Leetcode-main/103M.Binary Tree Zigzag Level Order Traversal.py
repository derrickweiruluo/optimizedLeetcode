# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        
        res = []
        curr_level = [root]
        depth = 0
        
        if not root: return res
        
        while curr_level:
            curr_vals = []
            next_level = []
            for node in curr_level:
                curr_vals.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
              
            if depth % 2 == 1:
                curr_vals = curr_vals[::-1]
            res.append(curr_vals)
            curr_level = next_level
            depth += 1
                
        
        
        
        
        return res
