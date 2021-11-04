'''
"""
https://leetcode.com/problems/binary-tree-upside-down/discuss/49410/Explain-the-question-and-my-solution-Python
https://xlinux.nist.gov/dads/HTML/binaryTreeRepofTree.html
Input: [1,2,3,4,5]
    1
   / \
  2   3
 / \
4   5
Output: return the root of the binary tree [4,5,2,#,#,3,1]
   4
  / \
 5   2
    / \
   3   1
The transform of the base three-node case is like below:
                         Root                   L
                         /  \                  /  \
                        L    R                R   Root
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: 
            return None
        if not root.left and not root.right: 
            return root
        left = self.upsideDownBinaryTree(root.left)
        root.left.left = root.right
        root.left.right = root
        root.left = root.right = None
        return left