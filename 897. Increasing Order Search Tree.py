# Intuition
# Don't need the condition of BST, just in-order output the whole tree.

# Straight forward idea here:
# result = inorder(root.left) + root + inorder(root.right)

# https://leetcode.com/problems/increasing-order-search-tree/discuss/165885/C%2B%2BJavaPython-Self-Explained-5-line-O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        def inorder(node, tail):
            if not node:
                return tail
            
            res = inorder(node.left, node)
            node.left = None
            node.right = inorder(node.right, tail)
            
            return res
        
        return inorder(root, None)
