'''
Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.

 

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        if not root:
            return False
        visited = set()
        
        def dfs(node):
            if not node:
                return False
            if k - node.val in visited:
                return True
            visited.add(node.val)
            return dfs(node.left) or dfs(node.right)
        
        return dfs(root)
        