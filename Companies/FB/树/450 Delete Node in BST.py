

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Time Complexity : O(h) - h = height of the tree.
# (Worst case Time Complexity : O(n) )

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        if not root: return None
        if root.val == key:
            if not root.left:
                return root.right
            if not root.right:
                return root.left

            # 下面这一行代码是精华，不断的找被delete的node 的 下一任，smallest greater node
            if root.left and root.right:
                successor = root.right
                while successor.left:
                    successor = successor.left
                root.val = successor.val
                root.right = self.deleteNode(root.right, successor.val)


        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        
        return root