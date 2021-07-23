# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:  # BFS + queue FAST!
        if not root: return []
        res = []
        queue = [(root, root.val, [root.val])]
        
        while queue:
            curr, val, ls = queue.pop(0)
            if not curr.left and not curr.right and val == targetSum:
                res.append(ls)
            if curr.left:
                queue.append((curr.left, val + curr.left.val, ls + [curr.left.val]))
            if curr.right:
                queue.append((curr.right, val + curr.right.val, ls + [curr.right.val]))   
        return res
            
        
    #. recursive, very slow
    # def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:   
    #     if not root: return []
    #     if not root.left and not root.right and root.val == targetSum:
    #         return [[root.val]]
    #     temp = self.pathSum(root.left, targetSum - root.val) + self.pathSum(root.right, targetSum - root.val)
    #     return [[root.val] + i for i in temp]


