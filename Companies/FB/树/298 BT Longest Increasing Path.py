'''
找一个longest的向下的 consecutive increasing path
The longest consecutive path needs to be 
from parent to child (cannot be the reverse).
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        
        if not root: return 0
        
        stack = [(root, 1)]
        res = 0
        
        while stack:
            node, cnt = stack.pop()
            if node.left:
                if node.left.val == node.val + 1:
                    stack.append((node.left, cnt + 1))
                else:
                    stack.append((node.left, 1))
            if node.right:
                if node.right.val == node.val + 1:
                    stack.append((node.right, cnt + 1))
                else:
                    stack.append((node.right, 1))
            res = max(res, cnt)
        
        return res



class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        
        if not root: return 0
        
        def dfs(node, cnt, prev):
            if not node:
                return cnt
            if node.val - prev == 1:
                cnt += 1
            else:
                cnt = 1
            left = dfs(node.left, cnt, node.val)
            right = dfs(node.right, cnt, node.val)
            return max(cnt, left, right)
        
        return dfs(root, 1, root.val)