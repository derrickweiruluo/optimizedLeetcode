'''
给一个BST preorder travesal的数组，返回该BST

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        def buildTree(nums, upperBound):
            if not nums or nums[-1] > upperBound:
                return None
            node = TreeNode(nums.pop())
            node.left = buildTree(nums, node.val)
            node.right = buildTree(nums, upperBound)
            return node
        
        
        # [8,5,1,7,10,12] -> [12,10,7,1,5,8]
        return buildTree(preorder[::-1], math.inf)