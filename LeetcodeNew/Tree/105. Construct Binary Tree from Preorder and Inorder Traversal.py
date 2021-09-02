"""
Example 1:

Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]
 
Constraints:

1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.


########
preorder.pop(0)为树的root
inorder_dict来定位该root的idx

创建完当前root之后，
root的左边，left ~ idx - 1 是左子树
root的右边， idx + 1 ~ right 是右子树


https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/discuss/34579/Python-short-recursive-solution.
"""
inorder_dict = {val: idx for idx, val in enumerate(inorder)}
        
        def build(left, right):
            if left > right: return
            
            root_idx = inorder_dict[preorder.pop(0)]
            root = TreeNode(inorder[root_idx])
            
            root.left = build(left, root_idx - 1)
            root.right = build(root_idx + 1, right)
            
            return root
        
        return build(0, len(inorder) - 1)
