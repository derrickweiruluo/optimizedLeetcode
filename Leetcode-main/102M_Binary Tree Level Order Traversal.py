# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        curr_level = [root]
        
        if not root: return res
        
        while curr_level:
            curr_nodes = []
            next_level = []
            for node in curr_level:
                curr_nodes.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            
            res.append(curr_nodes)
            curr_level = next_level
            
        return res
