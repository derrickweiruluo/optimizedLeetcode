# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 标准二叉树的递归 + 一点数学
# complete的意义
# 递归：当左右深度一样的时候count，不一样的时候 1 + count左子树 + count右子树
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root: return 0
        
        def depth_left(node):
            depth = 0
            while node:
                depth += 1
                node = node.left
            return depth

        def depth_right(node):
            depth = 0
            while node:
                depth += 1
                node = node.right
            return depth
        
        d_left = depth_left(root.left)
        d_right = depth_right(root.right)
        
        if d_left == d_right:
            return 2 ** (d_left + 1) - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        
        
    
