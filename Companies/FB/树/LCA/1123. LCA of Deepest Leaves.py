'''
如题目
865. Smallest Subtree with all the Deepest Nodes
找 LCA of all deepest leaves
'''

# # 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# test case1：完全平衡二叉树：[3,5,1,6,2,0,8,null,null]
# test case2: 平衡二叉树： [3,5,1,6,null,0,8,null,null]

class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        self.deepest = 0
        self.LCA = None
        
        def dfs(node, depth):
            self.deepest = max(self.deepest, depth)  # 每一次都update maxDepth
            if not node:
                return depth
            left = dfs(node.left, depth + 1)
            right = dfs(node.right, depth + 1)
            
            # 一路向南，LCA of deepest就是左右子树深度一样
            if left == right == self.deepest: # 一直往上更新，直到不满足，就停在LCA位置上了
                # print(node.val) # track the recursion update
                self.LCA = node
            return max(left, right)
        
        
        dfs(root, 0)
        # print(self.LCA.val) # test
        return self.LCA
    
###############
    
class Solution:  # without global variable, by LEE215 
    def lcaDeepestLeaves(self, root):
        def helper(root):
            if not root: return 0, None
            h1, lca1 = helper(root.left)
            h2, lca2 = helper(root.right)
            if h1 > h2: return h1 + 1, lca1
            if h1 < h2: return h2 + 1, lca2
            return h1 + 1, root
        return helper(root)[1]