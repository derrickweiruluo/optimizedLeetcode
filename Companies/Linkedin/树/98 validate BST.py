'''
'''

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def traverse(root, floor, ceiling):
            if not root:
                return True
            if not floor < root.val < ceiling:
                return False
            return traverse(root.left, floor, root.val) and traverse(root.right, root.val, ceiling)
        
        return traverse(root, -math.inf, math.inf)