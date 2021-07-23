# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        self.curr_tail = None
        
        def traverse(node):
            if not node:
                return              # backtracking step
            traverse(node.right)    # go all the way to the right
            traverse(node.left)     # when finish right, go the left
            
            node.right = self.curr_tail    # keep track of the tail pointer 
            node.left = None               # delete the left pointer
            self.curr_tail = node          # the global tail become the current node upon finishing right and left
        
        traverse(root)
        
