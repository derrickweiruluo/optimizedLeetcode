'''
BST 里面， Exactly 两个nodes 被互换了， recover 这个BST

'''
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        self.first, self.second, self.prev = None, None, None
        self.cur = root
        
        while self.cur:
            if self.prev and self.prev.val >= self.cur.val:
                if not self.first:
                    self.first = self.prev
                self.second = self.cur
            
            if not self.cur.left:
                self.prev = self.cur
                self.cur = self.cur.right
                
            else:
                predecessor = self.cur.left
                while predecessor.right != self.cur and predecessor.right:
                    predecessor = predecessor.right
                
                if not predecessor.right:
                    predecessor.right = self.cur
                    self.cur = self.cur.left
                else:
                    predecessor.right = None
                    self.prev = self.cur
                    self.cur = self.cur.right
                    
        # print(self.prev, self.first, self.second)
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