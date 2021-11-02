'''
156 二叉树调转 
二叉树调转 (只考虑当前层就好，重新排序后 递归left)
    X             Y
   / \    -->    / \
  Y   Z         Z   X
'''

class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root: return None
        if not root.left and not root.right: return root
        left = self.upsideDownBinaryTree(root.left)
        root.left.left = root.right
        root.left.right = root
        root.left = root.right = None
        return left