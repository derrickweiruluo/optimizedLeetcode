'''
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
'''

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def isEqual(left, right):
            if not left and not right:
                return True
            if left and not right:
                return False
            if right and not left:
                return False
            if left.val == right.val:
                return isEqual(left.left, right.right) and isEqual(left.right, right.left)
        
        return isEqual(root.left, root.right)