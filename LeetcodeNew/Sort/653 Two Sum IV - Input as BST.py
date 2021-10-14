'''
Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.

'''

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root: return False
        
        visited = set()
        def dfs(root):
            if not root:
                return False
            if k - root.val in visited:
                return True
            visited.add(root.val)
            return dfs(root.left) or dfs(root.right)

        return dfs(root)