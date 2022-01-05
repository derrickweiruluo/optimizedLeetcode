"""
node 多了 parent节点，但不给root，找他们的LCA

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
"""


''' 最优解注解
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/discuss/932499/Simple-Python-Solution-with-O(1)-space-complexity
The idea is fairly simple (and the same as finding the convergence point of 2 linked lists). We keep two pointers, p1 and p2. Originally, these pointers point to q and p, respectively. Then we follow their parent pointers until they point to the same node. When either of the pointers points to root, we set it to the other original starting node. For example, when p1 points to root (i.e p1.parent is None), assign q to p1.


node1: d1 to root
node2: d2 to root
when node1/node2 reach root, redirect to node2/node1
therefore the total distance to the root again after the redirection:

totalDist = 1 + d1 + 1 + d2, for node 1
totalDist = 1 + d2 + 1 + d1, for node 2

the converged route to the root, is the list of LCA
the first seen converged (same value), is the LCA 
At a minimum, the root of the tree is the LCA
'''
class Solution: # 最优解 ！！！
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        
        p1, p2 = p, q
        while p1 != p2:

            # 到顶之后，各自返回对方的起点，最终他们会相遇
            # A+B=B+A
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
