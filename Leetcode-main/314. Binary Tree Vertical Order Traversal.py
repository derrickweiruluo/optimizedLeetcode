# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        
        queue = collections.deque([(root, 0)])
        mapping = collections.defaultdict(list)
        
        while queue:
            node, pos = queue.popleft()
            if not node:
                continue
            mapping[pos].append(node.val) 
                
            queue.append((node.left, pos - 1))
            queue.append((node.right, pos + 1))
        
        return [mapping[pos] for pos in sorted(mapping)]
