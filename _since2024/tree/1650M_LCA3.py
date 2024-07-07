"""
Given two nodes of a binary tree p and q, return their lowest common ancestor (LCA).
"""

# difference btw LCA_1 is that:
# 1. this time, root node is not given
# 2. parent node is known in the treeNode datastructure
class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        
        node1, node2 = p, q
        while node1 != node2:
            node1 = node1.parent if node1.parent else q
            node2 = node2.parent if node2.parent else p
        
        return node1