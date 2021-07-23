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
    public TreeNode recoverFromPreorder(String S) {
        Deque <TreeNode> deque = new ArrayDeque<>();
        
        int length = S.length();
        int index = 0;
        
        while(index < length){
            int depth = 0;
            while(index < length && S.charAt(index) == '-'){
                depth ++; 
                index ++;
            }
            
            int val = 0;
            while(index < length && S.charAt(index) != '-'){
                val = val * 10 + (S.charAt(index) - '0'); 
                index ++;
            }
        
            while (deque.size() > depth) deque.pollLast();

            TreeNode node = new TreeNode(val);
            if(!deque.isEmpty()){
                TreeNode parent = deque.peekLast();
                if(parent.left == null) 
                    parent.left = node;
                else
                    parent.right = node;
            }
            deque.addLast(node);
        }
        System.out.println(deque.size());
        return deque.peekFirst();
    }
    
}
