'''
The boundary of a binary tree is the concatenation of the root, the left boundary, the leaves ordered from left-to-right, and the reverse order of the right boundary.
'''




class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        # The main idea is to carry the flag isleft and isight
        # in the dfs steps to help decide when to add node
        # values to the boundary array.
        
        if not root: return []
        res = [root.val]
        
        def dfs(node, isLeft, isRight):
            if not node: return
            
            if (not node.left and not node.right) or isLeft:
                res.append(node.val)
                
            if node.left and node.right:
                dfs(node.left, isLeft, False)
                dfs(node.right, False, isRight)
            else:
                dfs(node.left, isLeft, isRight)
                dfs(node.right, isLeft, isRight)
            
            
            if (node.left or node.right) and isRight:
                res.append(node.val)
        
        dfs(root.left, True, False)
        dfs(root.right, False, True)
        return res




# NOT THE BEST
class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        
        # preorder the left boundary which are not root or leaves
        def preorder_left(node):
            if not node or (not node.left and not node.right):
                return
            res.append(node.val)
            if node.left:
                preorder_left(node.left)
            else:
                preorder_left(node.right)
        
        def inorder_leave(node):
            if not node:
                return
            if node != root and (not node.left and not node.right):
                res.append(node.val)
            else:
                inorder_leave(node.left)
                inorder_leave(node.right)
        
        def postorder_right(node):
            if not node or (not node.left and not node.right):
                return
            if node.right:
                postorder_right(node.right)
            else:
                postorder_right(node.left)
            res.append(node.val)
            
        if not root: return res
        
        res = [root.val]
        preorder_left(root.left)
        inorder_leave(root)
        postorder_right(root.right)
        
        return res