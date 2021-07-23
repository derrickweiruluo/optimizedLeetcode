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
    
    private TreeNode  ans;
    
    private boolean recur(TreeNode root, TreeNode p, TreeNode q){
        if(root == null) return false;
        
        int top = (root == q || root == p)? 1:0;
        int right = recur(root.right, p, q)? 1:0;
        int left = recur(root.left, p, q)? 1:0;
        
        if(top + right + left > 1)  ans = root;
        return (top + right + left > 0);
    } 
    
     
    
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
       recur(root, p, q);
        return ans;
        
        
        
        
    }
}
