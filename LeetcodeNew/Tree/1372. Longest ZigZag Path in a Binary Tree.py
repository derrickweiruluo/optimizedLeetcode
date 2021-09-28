'''
You are given the root of a binary tree.

A ZigZag path for a binary tree is defined as follow:

Choose any node in the binary tree and a direction (right or left).
If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
Change the direction from right to left or from left to right.
Repeat the second and third steps until you can't move in the tree.

Return the longest ZigZag path contained in that tree.

############
Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).
Explanation
Recursive return [left, right, result], where:
left is the maximum length in direction of root.left
right is the maximum length in direction of root.right
result is the maximum length in the whole sub tree.

Complexity; Time O(N);  Space O(height)
'''

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if not node:
                return -1, -1, -1 
            # root.left's maxLen, root.right's maxLen and subtree's maxLen 
            left = dfs(node.left)
            right = dfs(node.right)
            return left[1] + 1, right[0] + 1, max(left[1] + 1, right[0] + 1, left[2], right[2])
        
        return dfs(root)[2]
