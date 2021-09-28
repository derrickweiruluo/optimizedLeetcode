'''
Given the root of a binary tree, return the lowest common ancestor of its deepest leaves.

Recall that:

The node of a binary tree is a leaf if and only if it has no children
The depth of the root of the tree is 0. if the depth of a node is d, the depth of each of its children is d + 1.
The lowest common ancestor of a set S of nodes, is the node A with the largest depth such that every node in S is in the subtree with root A.
Note: This question is the same as 865: https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/

# LCA of deepest leaves: 

DFS，记录depth， 如果左子树 大于/小于/等于 右子树
Solution 1: Get Subtree Height and LCA
helper function return the subtree height and lca and at the same time.
null node will return depth 0,
leaves will return depth 1.

'''

class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(node):
            if not node:
                return 0, None
            left = dfs(node.left)
            right = dfs(node.right)
            
            if left[0] > right[0]:
                return left[0] + 1, left[1]
            elif left[0] < right[0]: 
                return right[0] + 1, right[1]
            else:
                return left[0] + 1, node
        
        return dfs(root)[1]
