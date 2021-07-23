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
    private TreeNode first;
    private TreeNode second;
    private TreeNode prev;
    
    public void recoverTree(TreeNode root) {
        inorder (root);
        swap(first, second);
    }
    
    private void inorder(TreeNode root){
        if(root == null) return;
        inorder(root.left);
        if(prev != null && root.val < prev.val){
            second = root;
            if(first == null) first = prev;
            else return;
        }
        prev=root;
        inorder(root.right);
    }
    
    private void swap(TreeNode node1, TreeNode node2){
        int temp = node1.val;
        node1.val = node2.val;
        node2.val = temp;
    }
}
