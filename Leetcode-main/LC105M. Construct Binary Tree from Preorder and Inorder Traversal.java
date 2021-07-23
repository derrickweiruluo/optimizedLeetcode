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
    
    int preorderIndex = 0;
    HashMap <Integer, Integer> map = new HashMap();
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        for(int i=0; i<inorder.length; i++)
            map.put(inorder[i], i);
        return buildTree(preorder, inorder, 0, preorder.length-1);
    }
    
    private TreeNode buildTree (int[] preorder, int[] inorder, int left, int right){
        if(left > right) return null;
        int rootVal = preorder[preorderIndex];
        TreeNode root = new TreeNode(rootVal);
        preorderIndex ++;
        
        root.left = buildTree(preorder, inorder, left, map.get(rootVal)-1);
        root.right = buildTree(preorder, inorder, map.get(rootVal)+1, right);
        return root;
    }
}
