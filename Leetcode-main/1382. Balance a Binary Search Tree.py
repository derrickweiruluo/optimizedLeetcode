# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        def inorderTraverse(node):
            if not node:
                return
            inorderTraverse(node.left)
            sortedNodes.append(node)
            inorderTraverse(node.right)
        
        def buildBST(left, right):
            if left > right:
                return
            mid = (left + right) // 2
            root = sortedNodes[mid]
            root.left = buildBST(left, mid - 1)
            root.right = buildBST(mid + 1, right)
            return root
        
        sortedNodes = []
        inorderTraverse(root)
        return buildBST(0, len(sortedNodes) - 1)
