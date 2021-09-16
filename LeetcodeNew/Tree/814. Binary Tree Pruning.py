'''
Given the root of a binary tree, return the same tree where every subtree (of the given tree) not containing a 1 has been removed.

A subtree of a node node is node plus every node that is a descendant of node.

########思路
pruning requires 3 conditions: both left and right subtree is None
(either already a leaf node or pruned at bottom) && root.val == 0
'''

class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        
        '''pruning requires 3 conditions: both left and right subtree is None
        (either already a leaf node or pruned at bottom) && root.val == 0
        '''
        
        if not root.left and not root.right and root.val == 0:
            return None
        
        return root
        
