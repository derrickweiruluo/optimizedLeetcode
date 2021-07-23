class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        def isValid(node, floor, ceiling):
            if not node:
                return True
            if not floor < node.val < ceiling:
                return False
            
            return isValid(node.left, floor, node.val) and isValid(node.right, node.val, ceiling)
        
        return isValid(root, -math.inf, math.inf)
