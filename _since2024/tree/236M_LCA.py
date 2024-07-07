# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections


class Solution1:  # faster time with parent pointers w/ early return
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 1. The number of nodes in the tree is in the range [2, 105].
        # 2. We allow a node to be a descendant of ITSELF!
        child_to_parent = {root: None}
        queue = collections.deque([root])
        visited = set()
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    child_to_parent[node.left] = node
                    queue.append(node.left)
                if node.right:
                    child_to_parent[node.right] = node
                    queue.append(node.right)
        while p:
            visited.add(p)
            p = child_to_parent[p]
        while q not in visited:
            q = child_to_parent[q]
        return q


class Solution2:  # recursive
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, q, p)
        right = self.lowestCommonAncestor(root.right, q, p)
        if not left and not right:
            return root
        if left:
            return left
        if right:
            return right
        return None
    
    
    # https://leetcode.com/submissions/detail/600409983/
    # iterative
class Solution3:  # iterative
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # step 1, level-order-traversal to find the first p or q, and record the parent-child relationship at the meantime
        stack = [root]
        child_to_parent = {root: None}
        visted = set()
        while p not in child_to_parent or q not in child_to_parent:
            node = stack.pop()
            if node.left:
                child_to_parent[node.left] = node
                stack.append(node.left)
            if node.right:
                child_to_parent[node.right] = node
                stack.append(node.right)
        # step 2, from p or q, move up all the way to the root and keep track of visited
        while p:
            visted.add(p)
            p = child_to_parent[p]
        # step 3, from the other p/q, go up until it reached the visited set, which this node is the LCA
        while q not in visted:
            q = child_to_parent[q]
        
        return q