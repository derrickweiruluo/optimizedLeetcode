'''
如题 validate BST
'''

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        def morris(root):
            if not root: return None
            curr = root
            while curr:
                if not curr.left:
                    yield curr.val
                    curr = curr.right
                else:
                    prev = curr.left
                    while prev.right != None and prev.right != curr:
                        prev = prev.right
                    if prev.right == None:
                        prev.right = curr
                        curr = curr.left
                    elif prev.right == curr:
                        prev.right = None
                        yield curr.val
                        curr = curr.right
        prev = -math.inf
        for val in morris(root):
            if val <= prev: return False
            prev = val
        return True



class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def traverse(root, floor, ceiling):
            if not root:
                return True
            if not floor < root.val < ceiling:
                return False
            return traverse(root.left, floor, root.val) and traverse(root.right, root.val, ceiling)
        
        return traverse(root, -math.inf, math.inf)