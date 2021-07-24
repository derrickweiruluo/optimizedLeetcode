# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        
        mapping = collections.defaultdict(list)
        queue = collections.deque([(root, 0, 0)])   # cur_node, level and parent.val
        
        # BFS traversal using deque of tuple (node, level, parent_val)
        while queue:
            node, level, parent_val = queue.popleft()
            mapping[node.val] = [level, parent_val]
            
            if node.left:
                queue.append((node.left, level + 1, node.val))
            if node.right:
                queue.append((node.right, level + 1, node.val))
        
        if mapping[x][0] == mapping[y][0] and mapping[x][1] != mapping[y][1]:
            return True
        
        return False
