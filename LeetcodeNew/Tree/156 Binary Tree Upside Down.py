'''
"""
https://leetcode.com/problems/binary-tree-upside-down/discuss/49410/Explain-the-question-and-my-solution-Python
https://xlinux.nist.gov/dads/HTML/binaryTreeRepofTree.html

156.Binary-Tree-Upside-Down
此题的意思是：对于一个根-左-右的基本树状结构，右子树保证只有一个或为空。要求变形后，以左子树为根，把原来的根和右节点作为新根节点的右、左节点。

解决此题的思路应该坚定不移地寻找递归方案。

经过分析，应该能够发现，对于一个root,left,right的基本结构，变形后的新结构应该变为：递归(root->left)作为根，root作为右，root->left作为左。于是代码就非常好写了。

注意到递归(root->left)返回的是它的根节点。怎么把root作为递归(root->left)的右子树呢？只要不停地从根节点往右子树方向移动就可以了。

基本代码思路

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