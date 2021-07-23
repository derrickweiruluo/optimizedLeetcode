# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        
        if not root:
            return []
        res = []
        
        def dfs(node, path, res):
            path += str(node.val)
            if node.left:
                dfs(node.left, path + '->', res)
            if node.right:
                dfs(node.right, path + '->', res)
                
            if not node.left and not node.right:
                res.append(path)
            
        dfs(root, '', res)
        return res
