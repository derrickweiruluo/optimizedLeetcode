// 03-01-2021
// 3 ms beat 100% 
// 40 MB beat 60%

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

class Solution {

    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if(root == null) return null;
        if(root.val == q.val || root.val == p.val) return root;
        TreeNode left = p.val < q.val? p:q;
        TreeNode right = p.val < q.val? q:p;
        if(left.val<root.val && root.val<right.val){
            return root;
        }
        // find the subtree that has both nodes, recursive approach
        else if(root.val<right.val){
            return lowestCommonAncestor(root.right, left, right);
        }
        else {
            return lowestCommonAncestor(root.left, left, right);
        }
    }
}

// 2nd best solution
// class Solution {

//     private TreeNode lca;
    
//     private boolean recurTree(TreeNode currNode, TreeNode p, TreeNode q){
//         if(currNode == null){
//             return false;
//         }
//         int left = recurTree( currNode.left,  p,  q) ? 1:0;
//         int right = recurTree( currNode.right,  p,  q) ? 1:0;
//         int mid = (currNode==p || currNode==q) ? 1:0;
        
//         if(left+right+mid >=2){
//             lca = currNode;
//         }
//         return(left+right+mid>0);
//     }
    
//     public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
//         recurTree(root, p, q);
//         return lca;
//     }
// }
