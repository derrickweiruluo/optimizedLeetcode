'''
给两个Binary Tree的 head Nodes
p, q

Ask: are they the same tree?

Note:
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
'''


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q. left) and self.isSameTree(p.right, q.right)