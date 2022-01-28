

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        self.res = []
        
        def dfs(node, depth):
            if not node:
                return
            if len(self.res) == depth:
                self.res.append([])
            self.res[depth].append(node.val)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
            
        
        dfs(root, 0)
        return [sum(level) / len(level) for level in self.res]
        


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # BFS, Stack is O(m), m is the up to N / 2
        res = []
        if not root: return res
        
        stack = collections.deque([root])
        
        while stack:
            n = len(stack)
            curSum = 0
            for _ in range(n):
                node = stack.popleft()
                curSum += node.val
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            res += [curSum / n]
        
        return res