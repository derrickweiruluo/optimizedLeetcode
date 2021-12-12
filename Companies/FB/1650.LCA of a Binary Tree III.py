"""
Given two nodes of a binary tree p and q, return their lowest common ancestor (LCA).
Each node will have a reference to its parent node. The definition for Node is below:
## 题目：
给一棵树里面的两个node，不给root，找他们的LCA
"""


'''
         3
      /    \    
    5        1
  /   \     /  \
6      2   0    8
      / \
     7   4


For LCA of (4,6)
only searched: [3,5,6,2,7,4,5,1,0,8], printed the LCA: 5


For LCA of (5,6)
only searched: [3,5,1,0,8], does not print out the LCA, 默认是local解
'''

'''
The idea is fairly simple (and the same as finding the convergence point of 2 linked lists). We keep two pointers, p1 and p2. Originally, these pointers point to q and p, respectively. Then we follow their parent pointers until they point to the same node. When either of the pointers points to root, we set it to the other original starting node. For example, when p1 points to root (i.e p1.parent is None), assign q to p1.
'''
class Solution: # 最优解
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        
        p1, p2 = p, q
        while p1 != p2:
            p1 = p1.parent if p1.parent else q
            p2 = p2.parent if p2.parent else p
        
        return p1



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
