// 3ms, 86%; 40MB, 78%

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
    
    private boolean recur(TreeNode root, HashSet map){
        if(root == null) return false;
        
        int top = (map.contains(root)==true)? 1:0;
        int right = recur (root.right, map)? 1:0;
        int left = recur (root.left, map)? 1:0;
        
        if(top + left + right == 2) ans = root;
        
        return (top + left + right >0);
    }
    
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode[] nodes) {
        int num = nodes.length;
      
        HashSet <TreeNode> map = new HashSet<TreeNode>();
        for(int i=0; i<num; i++){
            map.add(nodes[i]);
        }
        if(map.contains(root)) return root;
        if(nodes.length == 1) return nodes[0];
        
        recur(root, map);

        return  ans;
    }
}
