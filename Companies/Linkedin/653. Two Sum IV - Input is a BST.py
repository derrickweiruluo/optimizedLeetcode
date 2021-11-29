'''
Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.

'''

class Solution: # interview solution
    # both O(n) but utilized the BST properties
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        nums = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            nums.append(node.val)
            inorder(node.right)
        
        inorder(root)
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] == k:
                return True
            elif nums[left] + nums[right] < k:
                left += 1
            else:
                right -= 1
        
        return False


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