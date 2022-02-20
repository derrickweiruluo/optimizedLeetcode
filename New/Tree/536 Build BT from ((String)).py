# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        
        root, stack, num = None, [], ""
        # num 用str记录方便处理负数
        
        n = len(s)
        
        for idx, char in enumerate(s):
            if char == ')':
                stack.pop() # if not the last node, parent will be there
            elif char == '(':
                continue
            else:
                num += char
                if idx + 1 == n or not s[idx + 1].isdigit():
                    curNode = TreeNode(num)
                    num = ""
                    if stack:
                        parent = stack[-1]
                        if parent.left:
                            parent.right = curNode
                        else:
                            parent.left = curNode
                    else:
                        root = curNode
                    stack.append(curNode)
        
        return root


# 不太熟熟的 recursive 解法
class Solution: 
    
    def str2tree(self, s: str) -> TreeNode:
        if not s or len(s) == 0:
            return None
        root, _ = self.dfs(s, 0)
        return root

    def dfs(self, s, i):
        start = i
        while i < len(s) and (s[i] == '-' or s[i].isdigit()): # negative sign or digit
            i += 1
        node = TreeNode(int(s[start : i]))
        if i < len(s) and s[i] == '(':
            i += 1      # skip '('
            node.left, i = self.dfs(s, i)
            i += 1      # skip ')'
        if i < len(s) and s[i] == '(': # still has '(', create right tree
            i += 1      # skip '('
            node.right, i = self.dfs(s, i)
            i += 1      # skip ')'
        return node, i