"""
公共祖先
Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

 
Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the tree.

"""
# ##思路：
# DFS, leave's info will pass recursively back
# to the upper level
# 两种情况, root 左右都有解，该root就是LCA
# 只有一边有解， 就把该解传上去，如果传到顶点还是只有一个解，then LCA 
# 因为另一个 target在 LCA的子树里面

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return
        if root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left and right: return root
        if left: return left
        if right: return right
