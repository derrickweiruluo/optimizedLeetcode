# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Just do a DFS and take the maximum of the depth from left child and right child.
Leaf nodes have depth 1.

Bottom-up approach
https://leetcode.com/problems/find-leaves-of-binary-tree/discuss/83822/Python-short-and-clear-solution-with-one-DFS-and-building-solution-on-the-go
https://leetcode.com/problems/find-leaves-of-binary-tree/discuss/153057/Logical-Thinking-with-Verbose-but-Clear-Code
https://leetcode.com/problems/find-leaves-of-binary-tree/discuss/83778/10-lines-simple-Java-solution-using-recursion-with-explanation

          1
         / \
        2   3
       / \     
      4   5   
      
height(4) = height(5) = height(3) = 1,
height(2) = 2,
height(1) = 3.
height(null) = 0

The time complecxity for this problem is O(HLogN) where H is the height of the tree and N is the number of nodes
"""
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = []
        
        def dfs(node):
            if not node:
                return 0
            depth = max(dfs(node.left), dfs(node.right)) + 1
            if len(res) < depth:  # len is 1 indexed, depth is zero-indexed
                res.append([])
            res[depth - 1].append(node.val)
            return depth
        
        dfs(root)
        return res
