'''
Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []
        if not root: return res
        
        queue = collections.deque([root])
        while queue:
            n = len(queue)
            curMax = -math.inf
            for _ in range(n):
                node = queue.popleft()
                curMax = max(curMax, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            res.append(curMax)
        
        return res

# DFS
class Solution(object):
    def largestValues(self, root):
        self.ans = []
        self.dfs(root, 0)
        return self.ans
    
    def dfs(self, node, level):
        if not node:
            return
        
        # expand list size
        if len(self.ans) == level:
            self.ans.append(node.val)
        # or, set the current max value
        else:
            self.ans[level] = max(self.ans[level], node.val)
        self.dfs(node.left, level+1)
        self.dfs(node.right, level+1)
                
            
        