"""
Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

"""


class Solution:  # Both O(N), 最优解
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        queue = collections.deque([(root, 0)])
        mapping = collections.defaultdict(list)
        left = right = 0
        
        while queue:
            node, col = queue.popleft()
            if node:
                mapping[col].append(node.val)
                left = min(left, col)
                right = max(right, col)
                queue.append((node.left, col - 1))
                queue.append((node.right, col + 1))
        
        return [mapping[x] for x in range(left, right + 1)]




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
