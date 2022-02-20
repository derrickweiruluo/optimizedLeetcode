'''
BST 里面， Exactly 两个nodes 被互换了， recover 这个BST
'''

#     3                 2
#   /   \             /   \
#  1     4   -->>>   1     4
#       /                 /
#     2                 3

# 3-->1-->3-->4-->2-->4


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.first, self.second, self.prev = None, None, None
        cur = root
        
        while cur:

            # initial check for current node for violation
            if self.prev and self.prev.val >= cur.val:
                if not self.first:
                    self.first = self.prev
                self.second = cur
                
            if not cur.left:
                # if no left, the right is always the next greater
                self.prev = cur
                cur = cur.right
            else:
                predecessor = cur.left
                while predecessor.right != cur and predecessor.right:
                    predecessor = predecessor.right

                if not predecessor.right:
                    # only build the parent pointer at rightMost
                    predecessor.right = cur
                    cur = cur.left
                else:
                    # update prev and navigate to cur.right
                    predecessor.right = None
                    self.prev = cur
                    cur = cur.right
        
        self.first.val, self.second.val = self.second.val, self.first.val



# 递归inorder 解，space O(H)
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        self.first, self.second, self.prev = None, None, None
        # self.prev = TreeNode(-math.inf)
        
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            if self.prev and self.prev.val >= root.val:
                if not self.first:
                    self.first = self.prev
                self.second = root
            self.prev = root
            inorder(root.right)
        
        inorder(root)
        print(self.first)
        print(self.second)
        self.first.val, self.second.val = self.second.val, self.first.val