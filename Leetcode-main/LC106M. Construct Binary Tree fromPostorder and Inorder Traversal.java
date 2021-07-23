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
    
    int postorderIndex;
    HashMap <Integer, Integer> map = new HashMap();
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        postorderIndex = postorder.length-1;
        for(int i=0; i<inorder.length; i++){
            map.put(inorder[i], i);
        }
        return buildTree(postorder, 0, inorder.length-1);
    }
    
    public TreeNode buildTree(int[] postorder, int left, int right){
        if(left > right) return null;
        int rootVal = postorder[postorderIndex];
        TreeNode root = new TreeNode(rootVal);
        
        int index = map.get(rootVal);
        postorderIndex --;
        
        root.right = buildTree(postorder, index+1, right);
        root.left = buildTree(postorder, left, index-1);
        return root;
    }
}
