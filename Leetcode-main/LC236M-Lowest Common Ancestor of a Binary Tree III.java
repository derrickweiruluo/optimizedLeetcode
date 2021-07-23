//20ms 94%; 40MB 21%

/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
};
*/

class Solution {
    
    private Node root;
    private Node ans;
    
    private Node findRoot(Node p, Node q){
        int pNum=0;
        int qNum=0;
        while(p.parent != null){
            p=p.parent;
            pNum++;
        }
        while(q.parent != null){
            q=q.parent;
            qNum++;
        }
        root = (pNum>qNum)?p:q;
        return root;
    }
    
    private boolean recur (Node root, Node p, Node q) {
        if(root == null) return false;
        
        int top = (root==p || root==q)? 1:0;
        int right = recur(root.right, p, q)? 1:0;
        int left = recur(root.left, p ,q)? 1:0;
        
        if(top + left + right == 2){
            ans = root;
        }
        return (top + right + left > 0);
    }
    
    public Node lowestCommonAncestor(Node p, Node q) {
        findRoot (p, q);
        recur(root, p ,q);
        return ans;
    }
}
