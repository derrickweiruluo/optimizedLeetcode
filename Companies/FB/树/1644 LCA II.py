# p, q 可能不在树里面 --> Null

'''
Given the root of a binary tree, return the lowest common ancestor (LCA) of two given nodes, p and q. 
If either node p or q does not exist in the tree, return null. 
All values of the nodes in the tree are unique.
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

'''
Clarification:
每个node的唯一性 --> early return

'''



class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        self.res = None
        
        def dfs(node, p, q):
            if not node:
                return False
            # if self.res:
            #     return False
            top = 1 if (node == q or node == p) else 0
            left = 1 if dfs(node.left, p, q) else 0
            right = 1 if dfs(node.right, p, q) else 0
            if top + left + right == 2:
                self.res = node
                # return False
            return top + left + right > 0
        
        dfs(root, p, q)
        return self.res