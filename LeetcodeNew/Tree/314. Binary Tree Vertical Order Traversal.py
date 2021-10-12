"""
Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

"""


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = collections.deque([(root, 0)])
        mapping = collections.defaultdict(list)
        
        while queue:
            node, verPos = queue.popleft()  # make sure the result always go from left to right
            if node:
                queue.append((node.left, verPos - 1))
                queue.append((node.right, verPos + 1))
                mapping[verPos].append(node.val)
        
        return [mapping[i] for i in sorted(mapping)]




class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root: return []
        
        queue = collections.deque([(root, 0)])
        mapping = collections.defaultdict(list)
        
        while queue:
            node, pos = queue.popleft()  # make sure the result always go from left to right
            if node:
                mapping[pos].append(node.val)
                queue.append((node.left, pos - 1))
                queue.append((node.right, pos + 1))
        
        return [mapping[i] for i in sorted(mapping)]
