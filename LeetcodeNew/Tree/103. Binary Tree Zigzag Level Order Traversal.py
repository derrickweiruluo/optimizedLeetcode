"""
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

套娃，只需记录层数即可
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:  # more concised code
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = collections.deque([root])
        while queue:
            cur = []
            for _ in range(len(queue)):
                node = queue.popleft()
                cur.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(cur)
        
        for i in range(len(res)):
            if i % 2:
                res[i] = res[i][::-1]


class Solution2:  # older code
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root: return []
        
        res = []
        cur_level = [root]
        level = 0
        
        while cur_level:
            level += 1
            next_level = []
            cur_val = []
            for node in cur_level:
                cur_val.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            
            if level % 2 == 0:
                res.append(cur_val[::-1])
            else:
                res.append(cur_val)
            cur_level = next_level
        
        return res
