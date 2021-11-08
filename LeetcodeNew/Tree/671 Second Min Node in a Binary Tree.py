"""
https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/discuss/233767/Python-iterative-and-recursive-preorder-solutions-beats-100
Given a non-empty special binary tree consisting of nodes with the non-negative value,
where each node in this tree has exactly two or zero sub-node.
If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes.
Given such a binary tree, you need to output the second minimum value
in the set made of all the nodes' value in the whole tree.
If no such second minimum value exists, output -1 instead.
Example 1:
Input:
    2
   / \
  2   5
     / \
    5   7
Output: 5
Explanation: The smallest value is 2, the second smallest value is 5.
Example 2:
Input:
    2
   / \
  2   2
Output: -1
Explanation: The smallest value is 2, but there isn't any second smallest value.
"""
"""
Based on the special property of the tree, `
we can guarantee that the root node is the smallest node in the tree. 
We just have to recursively traverse the tree and find a node that is bigger than the root node 
but smaller than any existing node we have come across.
"""


class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        
        '''
        More formally, the property root.val = min(root.left.val, root.right.val) always holds.
        '''
        self.res = math.inf


        # 这道题目的特殊设定，root is garenteed to be the MIN Node
        # 所以只要找出比root大的，且min(res, cur)就可以了
        def dfs(node):
            if not node:
                return
            if root.val < node.val < self.res:
                print(node.val)
                self.res = node.val
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        if self.res == math.inf:
            return -1
        return self.res