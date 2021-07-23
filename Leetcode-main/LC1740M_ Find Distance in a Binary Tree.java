/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int findDistance(TreeNode root, int p, int q) {
        TreeNode lca = LCA(root, p, q);
        return dist(lca, p, 0) + dist(lca, q, 0);
    }
    
    private int dist(TreeNode root, int target, int travel) {
        
        if(root == null) return -1;
        if(root.val == target) return travel;
        
        int travelLeft = dist(root.left, target, travel + 1);
        if(travelLeft == -1)  return dist(root.right, target, travel + 1);
        
        return travelLeft;
    }
    
    private TreeNode LCA(TreeNode currNode, int p, int q) {
        
        if(currNode == null) return null;
        if(currNode.val == p || currNode.val == q) return currNode;

        TreeNode left = LCA(currNode.left, p, q);
        TreeNode right = LCA(currNode.right, p, q);
        
        if((left != null && right != null)) return currNode; 
                
        return left == null? right: left;
    }
    
}
