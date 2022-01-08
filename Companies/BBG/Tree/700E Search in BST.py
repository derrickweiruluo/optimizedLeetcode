'''
如题
'''

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return None
        cur = root
        while cur:
            if cur.val == val:
                return cur
            if val > cur.val:
                cur = cur.right
            else:
                cur = cur.left


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return None
        if val == root.val:
            return root
        if val > root.val: return self.searchBST(root.right, val)
        else: return self.searchBST(root.left, val)