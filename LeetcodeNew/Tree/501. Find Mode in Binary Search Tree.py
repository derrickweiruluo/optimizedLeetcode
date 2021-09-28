'''
Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.

If the tree has more than one mode, return them in any order.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.

##########
For example:
Given BST [1,null,2,2],
   1
    \
     2
    /
   2
return [2].

'''

https://leetcode.com/problems/find-mode-in-binary-search-tree/discuss/98100/Java-4ms-Beats-100-Extra-O(1)-solution-No-Map

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        cache = collections.defaultdict(int)
        self.maxFreq = -1
        self.preorder(root, cache)
        return [nodeVal for nodeVal, freq in cache.items() if freq == self.maxFreq]
    
    def preorder(self, node, cache):
        if not node:
            return
        cache[node.val] += 1
        self.maxFreq = max(self.maxFreq, cache[node.val])
        self.preorder(node.left, cache)
        self.preorder(node.right, cache)
