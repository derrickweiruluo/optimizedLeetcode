'''
Given the roots of two binary search trees, root1 and root2, return true if and only if there is a node in the first tree and a node in the second tree whose values sum up to a given integer target.


先遍历第一棵树，记录所有的node.val
遍历第二棵树，如果发现有任何target - cur.val 在 visited1里面, True
'''

class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        visited1, visited2 = set(), set()
        
        def dfs(root):
            if not root:
                return
            visited1.add(root.val)
            dfs(root.left)
            dfs(root.right)
            
        def dfs2(root):
            if not root:
                return False
            if target - root.val in visited1:
                return True
            return dfs2(root.left) or dfs2(root.right)
        
        dfs(root1)
        return dfs2(root2)