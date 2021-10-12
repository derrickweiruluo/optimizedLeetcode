'''
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

       1
      /  \
    2      3
     \       \
       5       4

res = [1,3,4]

'''
# 右向遍历，dfs的时候每一层都检查depth == len(res)，来确保每层只加最右边的且只加一次
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(node, level):
            if not node: 
                return
            if len(res) == level:  # 只加append一次，以当前解的长度 == depth来控制
                res.append(node.val)
            dfs(node.right, level + 1)
            dfs(node.left, level + 1)
        
        dfs(root, 0)
        return res