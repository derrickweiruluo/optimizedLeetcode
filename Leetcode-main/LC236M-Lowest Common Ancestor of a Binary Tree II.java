// 20ms,95%; 

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
    
    private TreeNode ans;
    
    private boolean recur(TreeNode root, TreeNode p, TreeNode q){
        if (root == null) return false;
        
        int top = (root == p || root == q)? 1:0;
        int right = recur (root.right, p, q)? 1:0;
        int left = recur (root.left, p, q)? 1:0;
        
        if(top + left + right == 2) ans = root;
        
        return (top + left + right >0);
    }
    
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        return (recur(root, p ,q))? ans:null;

    }
}
