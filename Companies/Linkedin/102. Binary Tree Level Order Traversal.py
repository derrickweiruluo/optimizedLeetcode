# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""
https://leetcode.com/problems/binary-tree-level-order-traversal/
树遍历
"""
import collections
class Solution:  # 11/2021
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root: return []
        
        queue = collections.deque([root])
        res = []
        
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
                  
        return res



class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root: return []
        
        res = []   # [[lev 1], [lev 2], [lev 3]] 
        cur_level = [root]
        
        while cur_level:
            next_level = []
            cur_val = []
            for node in cur_level:
                cur_val.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            
            res.append(cur_val)
            cur_level = next_level
        
        return res
