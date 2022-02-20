"""
https://leetcode.com/problems/find-duplicate-subtrees/discuss/106016/O(n)-time-and-space-lots-of-analysis
-
Example 1:
        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4
The following are two duplicate subtrees:
      2
     /
    4
and
    4
We can serialize each subtree. For example, the tree
   1
  / \
 2   3
    / \
   4   5
can be represented as the serialization 1,2,#,#,3,4,#,#,5,#,#,
which is a unique representation of the tree.
"""



# We can serialize subtrees while traversing the tree, and then compare the serializations to see if there are duplicates.
# The post-order traversal is natural here.
# As for the construction of the serialization string, we can apply either the pre-order or the post-order. 
# The in-order is inappropriate here because trees as shown below will have the same serializations if in-order.

#    0
#   /
#  0

#  0
#   \
#    0
# Since we only need to return the root node of any one of duplicate subtrees of the same kind, we utilize a dictionary that maps a serialization string to its appearances. And we add a subtree root to result only if its serialization string appears once.


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        memo = {}
        res = []
        self.dfs(root, res, memo)
        return res
    
    def dfs(self, node, res, memo):
        if not node: 
            return '#'  # termination of a tree
        serial = str(node.val) + 'l' + self.dfs(node.left, res, memo) + 'r' + self.dfs(node.right, res, memo)
        memo[serial] = memo.get(serial, 0) + 1
        
        if memo[serial] == 2:  # 只等于2是因为 2后面的就是重复的解，所以 if == 2
            res.append(node)
        return serial


class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        
        ## Post order traversal
        
        res = []
        memo = {}
        self.dfs(root, res, memo)
        return res
    
    def dfs(self, node, res, memo) -> str:
        if not node:
            return ""
        
        # serializing step, add spacers between root, left and right
        # the original code will fail on new test case: [2,1,11,11,null,1], 
        # this is because str(11) = str(1) == str(1) + str(11)
        serial = str(node.val) + "." + self.dfs(node.left, res, memo) + "," + self.dfs(node.right, res, memo)
        memo[serial] = memo.get(serial, 0) + 1
        
        # count for this serialized tree, whether is duplicate
        if memo[serial] == 2:
            res.append(node)
        
        return serial