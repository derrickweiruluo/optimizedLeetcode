"""
Given the root of a binary tree, return the lowest common ancestor (LCA) of two given nodes, p and q.
 If either node p or q does not exist in the tree, return null. All values of the nodes in the tree are unique.

According to the definition of LCA on Wikipedia: "The lowest common ancestor of two nodes p and q in a 
binary tree T is the lowest node that has both p and q as descendants (where we allow a node to be a descendant of itself)". 
A descendant of a node x is a node y that is on the path from node x to some leaf node.
"""


# difference between LCA_1, this one, either p or q node should be non-exisitence
class Solution_2024:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.lca = None

        def dfs(node):
            if not node:
                return False
            top = 1 if (node == p or node == q) else 0
            left = 1 if dfs(node.left) else 0
            right = 1 if dfs(node.right) else 0

            if top + left + right == 2:
                self.lca = node
                return
            return (top + left + right == 1)
        dfs(root)
        return self.lca


class Solution_2021:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        self.LCA = None
        
        def dfs(node, p, q):
            if not node:
                return False
            top = 1 if (node == p or node == q) else 0
            left = 1 if dfs(node.left, p, q) else 0
            right = 1 if dfs(node.right, p, q) else 0
            
            if top + left + right == 2:
                self.LCA = node
            
            return top + left + right > 0
            
        dfs(root, p ,q)
        return self.LCA