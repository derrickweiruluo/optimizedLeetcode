

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
Note: This is a BST
Avoid meaningless search

only visit left-subtree if node.val > low
only visit right-subtree if node.val < high
The valid range is [low, high]:: inclusive!!!
'''
# https://www.youtube.com/watch?v=wGXB9OWhPTg
class Solution:  # O(1) Space, via Morris Traversal

    # Inorder iterative traversal of a binary tree without stack or recursion. This traversal is called Morris traversal.
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # Morris order traversal
        res = 0
        while root:
            if not root.left:
                # do sth
                if low <= root.val <= high:
                        res += root.val
                root = root.right
            else:
                predecessor = root.left
                while predecessor.right != root and predecessor.right:
                    predecessor = predecessor.right
                    
                if not predecessor.right:  # 第一次还不存在 predeessor -> node link, build it, go left
                    predecessor.right = root
                    root = root.left       # 继续走左道
                    
                else:  # 第2次visit, break the temp link of a node's predecesor
                    # do sth
                    if low <= root.val <= high:
                        res += root.val
                    predecessor.right = None
                    root = root.right       # 开始探索柚子树
        
        return res


########### BELOW IS THE MORRIS TEMPLATE
    def morrisTraversal(self, root):
        while root:
            if not root.left:
                #####
                # do sth
                #####
                root = root.right
            else:
                predecessor = root.left
                while predecessor.right != root and predecessor.right:
                    predecessor = predecessor.right
                    
                if not predecessor.right:  # 第一次还不存在 predeessor -> node link, build it, go left
                    predecessor.right = root
                    root = root.left       # 继续走左道
                    
                else:  # 第2次visit, break the temp link of a node's predecesor
                    #####
                    # do sth
                    #####
                    predecessor.right = None
                    root = root.right       # 开始探索柚子树





class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        self.res = 0
        
        def dfs(node, lo, hi):
            if not node: return
            if lo <= node.val <= hi:
                self.res += node.val
            if node.val > lo:
                dfs(node.left, lo, hi)
            if node.val < hi:
                dfs(node.right, lo, hi)
        
        dfs(root, low, high)
        return self.res