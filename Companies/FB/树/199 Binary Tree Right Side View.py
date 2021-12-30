"""
Given a binary tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.
Example:
Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:
   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
"""

import collections

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Complexity

# Time: O(N), where N <= 100 is the nunber of nodes in the binary tree.
# Space: O(H), where H is the height of the binary tree, it's the depth of stack memory

# Space complexity O(logn) for stack frame during recursion.
# Time complexity is O(n) because it still visits all nodes.

class Solution: #DFS, O(N) and O(H)
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []
        
        def dfs(node, level):
            if not node:
                return
            if level == len(res):
                res.append(node.val)
            dfs(node.right, level + 1)
            dfs(node.left, level + 1)
        
        dfs(root, 0)
        return res



'''
Time complexity: O(N) since one has to visit each node.

Space complexity: O(D) to keep the queues, where D is a tree diameter. Let's use the last level to estimate the queue size. This level could contain up to N/2N/2 tree nodes in the case of complete binary tree.

'''

class Solution:
    def rightSideView(self, root: TreeNode):
        if not root:
            return []
        queue, res = collections.deque([root]), []
        while queue:
            res.append(queue[-1].val)
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res