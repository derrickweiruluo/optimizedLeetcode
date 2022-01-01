# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# test case: [1,2,3,4,5,6,8,9,10,10]
'''
if root is a complete tree ,
dfs(root) return the count of nodes in a tree,
otherwise it will return -1

If a tree is a complete FULL tree,
it must have 1,3,7,15,31..nodes,
which is pow of 2 minus 1.
And for x = 2^k -1, x has a property that x & (x+1) == 0.

For a complete tree, it must satify at least one of the following condition:
if left subtree is a full tree with l nodes,
right subtree must have r nodes that l / 2 <= r <= l
if right subtree is a full tree with r nodes,
left subtree must have l nodes that r <= l <= r * 2 + 1.

Time O(N), Space O(height)'''

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        
        def check(num):
            for i in range(30):
                if num == 2 ** i - 1:
                    return True
            return False
        
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            if check(left) and left // 2 <= right <= left:
                # 如果左子树complete， 那右子树要么是complete少一层，要么同样层数不complete
                return left + right + 1
                # 反之, 如果左子树不完整，柚子树完整，那么 left 一定比右边高一层
            if check(right) and right <= left <= right * 2 + 1:
                return left + right + 1

            # 如果两个都不完整，-1, 往上递归的时候，上层的check也会fail掉，root最终也返回 -1
            return -1
            
        # print(dfs(root))
        return dfs(root) > 0