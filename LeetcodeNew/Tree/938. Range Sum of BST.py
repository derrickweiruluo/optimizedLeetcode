'''
Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

'''

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.res = 0
        self.traverse(root, low, high)
        return self.res
    
    def traverse(self, root, lo, hi):
        if not root:
            return
        if lo <= root.val <= hi:
            self.res += root.val
        if root.val > lo:
            self.traverse(root.left, lo, hi)
        if root.val < hi:
            self.traverse(root.right, lo, hi)