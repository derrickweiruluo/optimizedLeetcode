import collections
import math

"""
Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.


Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
"""


def verticalOrder(root):
    if not root:
        return []
    left_bound, right_bound = math.inf, -math.inf

    # queue is for level-order traversal which keep track of the top-down relationship
    queue = collections.deque()
    queue.append((root, 0))
    
    # dict(list) is for vertical relationship, which key is column index, value is the list of node from top down
    tree_vertical_memory = collections.defaultdict(list)

    while queue:
        for _ in range(len(queue)):
            node, column_index = queue.popleft()
            tree_vertical_memory[column_index].append(node.val)
            left_bound = min(left_bound, column_index)
            right_bound = max(right_bound, column_index)
            if node.left:
                queue.append((node.left, column_index - 1))
            if node.right:
                queue.append((node.right, column_index + 1))
    return [tree_vertical_memory[i] for i in range(left_bound, right_bound + 1)]
