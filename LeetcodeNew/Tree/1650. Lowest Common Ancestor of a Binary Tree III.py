"""
Given two nodes of a binary tree p and q, return their lowest common ancestor (LCA).
Each node will have a reference to its parent node. The definition for Node is below:
## 题目：
给一棵树里面的两个node，不给root，找他们的LCA

# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        root = self.findRoot(p, q)
        return self.dfs(root, p, q)
    
    def findRoot(self, p, q):
        depth1 = depth2 = 0
        while p.parent:
            p = p.parent
            depth1 += 1
        while q.parent:
            q = q.parent
            depth2 += 1
        return p if depth1 > depth2 else q
    
    def dfs(self, root, p, q):
        if not root:
            return
        if root == p or root == q:
            return root
        left = self.dfs(root.left, p, q)
        right = self.dfs(root.right, p, q)
        if left and right:
            return root
        if left:
            return left
        if right:
            return right
