# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        
        queue = collections.deque([(root, 0, 0)])  # an queue of list of tuple
        mapping = collections.defaultdict(list)
        
        while queue:
            node, column, depth = queue.popleft()
            if not node:
                continue
            mapping[column].append((node.val, depth))
            queue.append((node.left, column - 1, depth + 1))
            queue.append((node.right, column + 1, depth + 1))
        
        res = []
        for column in sorted(mapping):
            res.append(mapping[column])
        print(res)
        for idx, item in enumerate(res):
            item.sort(key=lambda x: (x[1], x[0]))
            # item.sort(key=lambda x: x[1])
            res[idx] = [val for val, depth in item]
        
        return res
        
        
        return res
