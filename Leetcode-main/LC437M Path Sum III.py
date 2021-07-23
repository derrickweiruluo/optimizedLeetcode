# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        self.count = 0
        presum_dict = defaultdict(lambda : 0)
        presum_dict[0] = 1
        
        def preorder(node, curr_sum):
            if not node:
                return None
            curr_sum += node.val
            self.count += presum_dict[curr_sum - targetSum]
            presum_dict[curr_sum] += 1
            preorder(node.left, curr_sum)
            preorder(node.right, curr_sum)
            presum_dict[curr_sum] -= 1
            
        preorder(root, 0)
        return self.count
