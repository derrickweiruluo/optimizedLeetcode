# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.dq = collections.deque([root])
        while self.dq[0].right:
            node = self.dq.popleft()
            self.dq.extend([node.left, node.right])

    def insert(self, v: int) -> int:
        parent = self.dq[0]
        if parent.left:
            parent.right = TreeNode(v)     
            self.dq.extend([parent.left, parent.right])
            self.dq.popleft()
        else:
            parent.left = TreeNode(v)    
        return parent.val

    def get_root(self) -> TreeNode:
        return self.root